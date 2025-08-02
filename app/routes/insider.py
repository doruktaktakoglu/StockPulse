from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas
from typing import List


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all", response_model=List[schemas.InsiderTradeBase])
def read_insider_trades(db: Session = Depends(get_db)):
    return crud.get_all_insider_trades(db)


@router.get("/{ticker}", response_model=List[schemas.InsiderTradeBase])
def get_insider_trades_by_ticker(ticker: str, db: Session = Depends(get_db)):
    return crud.get_insider_trades_by_ticker(db, ticker)


@router.post("/{ticker}")
def ingest_insider_trades(ticker: str, db: Session = Depends(get_db)):
    from app.ingestion import scrape_openinsider_insider_trades
    scrape_openinsider_insider_trades(db, ticker.upper())
    return {"message": f"Insider trades for {ticker.upper()} ingested successfully."}

