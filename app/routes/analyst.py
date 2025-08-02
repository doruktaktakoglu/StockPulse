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

@router.get("/all", response_model=List[schemas.AnalystRatingBase])
def read_analyst_ratings(db: Session = Depends(get_db)):
    return crud.get_all_analyst_ratings(db)

@router.get("/{ticker}", response_model=List[schemas.AnalystRatingBase])
def get_analyst_ratings_by_ticker(ticker: str, db: Session = Depends(get_db)):
    return crud.get_analyst_ratings_by_ticker(db, ticker)


@router.post("/{ticker}")
def ingest_analyst_rating(ticker: str, db: Session = Depends(get_db)):
    from app.ingestion import ingest_finnhub_analyst_ratings
    ingest_finnhub_analyst_ratings(db, ticker.upper())
    return {"message": f"Analyst ratings for {ticker.upper()} ingested successfully."}


