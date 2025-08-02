from app.database import SessionLocal, init_db
from app.ingestion import ingest_finnhub_analyst_ratings, scrape_openinsider_insider_trades

init_db()
db = SessionLocal()

ticker = "AAPL"  # example ticker

print(f"Ingesting analyst ratings for {ticker} from Finnhub...")
ingest_finnhub_analyst_ratings(db, ticker)

print(f"Scraping insider trades for {ticker} from OpenInsider...")
scrape_openinsider_insider_trades(db, ticker)

db.close()
