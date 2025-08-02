import os
import requests
from datetime import date, datetime
from sqlalchemy.orm import Session
from app import models
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()  # Load API keys from .env

FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")


def ingest_finnhub_analyst_ratings(db: Session, ticker: str):
    """
    Fetch analyst ratings from Finnhub for a ticker and save to DB.
    """
    url = f"https://finnhub.io/api/v1/stock/recommendation?symbol={ticker}&token={FINNHUB_API_KEY}"
    response = requests.get(url)
    data = response.json()

    print(data)
    if not data:
        print("No analyst ratings data received from Finnhub.")
        return

    # Clear old ratings for this ticker (optional)
    db.query(models.AnalystRating).filter(models.AnalystRating.ticker == ticker).delete()
    db.commit()

    for entry in data:
        rating_date = datetime.strptime(entry['period'], "%Y-%m-%d").date()
        rating = entry.get('rating', 'N/A')

        analyst_rating = models.AnalystRating(
            ticker=ticker,
            analyst="Finnhub",  # Generic analyst name
            rating=rating,
            date=rating_date
        )
        db.add(analyst_rating)
    db.commit()


def scrape_openinsider_insider_trades(db: Session, ticker: str):
    """
    Scrape recent insider trades for a ticker from OpenInsider.
    """
    url = f"http://openinsider.com/screener?s={ticker}&o=&pl=&ph=&ll=&lh=&fd=0&fdr=&td=30&tdr=&fdly=&fddly=&sortcol=0&sortdir=&s=0&ps=500"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Delete existing trades for this ticker (optional)
    db.query(models.InsiderTrade).filter(models.InsiderTrade.ticker == ticker).delete()
    db.commit()

    table = soup.find("table", {"class": "tinytable"})
    if not table:
        print("Could not find trades table on OpenInsider")
        return

    rows = table.find_all("tr")[1:]  # skip header

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 10:
            continue

        # Map columns according to the actual table structure
        try:
            name = cols[5].text.strip()
            role = ""  # No role column visible, leave empty or scrape elsewhere if needed
            date_str = cols[2].text.strip()
            transaction_type = cols[7].text.strip()
            shares_text = cols[9].text.replace(",", "").strip()
            price_text = cols[8].text.replace("$", "").replace(",", "").strip()

            shares = int(shares_text) if shares_text and shares_text != "-" else 0
            price = float(price_text) if price_text and price_text != "-" else 0.0
            value = shares * price

            trade_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except Exception as e:
            print(f"Skipping row due to parse error: {e}")
            continue

        trade = models.InsiderTrade(
            ticker=ticker,
            name=name,
            role=role,
            date=trade_date,
            transaction_type=transaction_type,
            shares=shares,
            value=value
        )
        db.add(trade)

    db.commit()


def scrape_alphaspread_dcf(ticker: str):
    url = f"https://www.alphaspread.com/security/nyse/{ticker.lower()}/dcf-valuation/base-case"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    base_case_elem = soup.find("div", class_="valuation-scenario-value")
    if base_case_elem:
        base_case_text = base_case_elem.get_text(strip=True).replace("USD", "").strip()
    else:
        base_case_text = None

    return base_case_text


def scrape_valueinvesting_dcf(ticker: str):
    url = f"https://valueinvesting.io/{ticker.upper()}/valuation/dcf-growth-exit-5y"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all divs with class "tiny" and look for the one with text "Fair Price"
    fair_price_label = None
    for div in soup.find_all("div", class_="tiny"):
        if div.get_text(strip=True).lower() == "fair price":
            fair_price_label = div
            break

    if fair_price_label:
        # Get previous sibling or parent div that contains the .norm class with the number
        parent = fair_price_label.parent
        if parent:
            dcf_elem = parent.find("div", class_="norm")
            if dcf_elem:
                dcf_text = dcf_elem.get_text(strip=True).replace("USD", "").strip()
                return dcf_text

    return None


