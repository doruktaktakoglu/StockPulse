from sqlalchemy.orm import Session
from app import models

def get_all_insider_trades(db: Session):
    return db.query(models.InsiderTrade).all()

def get_all_analyst_ratings(db: Session):
    return db.query(models.AnalystRating).all()

def create_insider_trade(db: Session, trade: models.InsiderTrade):
    db.add(trade)
    db.commit()
    db.refresh(trade)
    return trade

def create_analyst_rating(db: Session, rating: models.AnalystRating):
    db.add(rating)
    db.commit()
    db.refresh(rating)
    return rating


