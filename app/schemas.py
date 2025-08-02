from pydantic import BaseModel, Field
from datetime import date, datetime

class InsiderTradeBase(BaseModel):
    ticker: str
    name: str
    role: str
    date: date
    transaction_type: str
    shares: int
    value: float

    class Config:
        orm_mode = True

class AnalystRatingBase(BaseModel):
    ticker: str
    analyst: str
    rating: str
    date: date

    class Config:
        orm_mode = True

class DCFValuation(BaseModel):
    ticker: str
    alphaspread: dict
    valueinvesting: dict
    timestamp: datetime = Field(default_factory=datetime.now)
