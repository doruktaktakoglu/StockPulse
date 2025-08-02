from fastapi import APIRouter, HTTPException
from app.ingestion import scrape_alphaspread_dcf, scrape_valueinvesting_dcf

router = APIRouter()

@router.get("/{ticker}", tags=["DCF Valuation"])
def get_dcf_valuation(ticker: str):
    try:
        alphaspread_data = scrape_alphaspread_dcf(ticker)
        valueinvesting_data = scrape_valueinvesting_dcf(ticker)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error scraping data: {e}")

    return {
        "ticker": ticker.upper(),
        "alphaspread": alphaspread_data,
        "valueinvesting": valueinvesting_data
    }
