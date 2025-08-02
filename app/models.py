from sqlalchemy import Column, Integer, String, Date, Float
from app.database import Base

class InsiderTrade(Base):
    __tablename__ = "insider_trades"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    name = Column(String)
    role = Column(String)
    date = Column(Date)
    transaction_type = Column(String)
    shares = Column(Integer)
    value = Column(Float)

class AnalystRating(Base):
    __tablename__ = "analyst_ratings"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    analyst = Column(String)
    rating = Column(String)
    date = Column(Date)

class DcfValuation(Base):
    __tablename__ = "dcf_valuations"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    source = Column(String)  # e.g., "alphaspread" or "valueinvesting"
    value = Column(Float)
    date = Column(Date)  # date of scraping or report (optional)
