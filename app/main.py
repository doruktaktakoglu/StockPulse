from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes import insider, analyst, signals, dcf
from app.database import init_db

app = FastAPI(title="StockPulse")

# Initialize DB on startup
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield
    # Shutdown (if needed)
    pass

# Register routers
app.include_router(insider.router, prefix="/insider-trades", tags=["Insider Trades"])
app.include_router(analyst.router, prefix="/analyst-ratings", tags=["Analyst Ratings"])
app.include_router(signals.router, prefix="/signals", tags=["Signals"])
app.include_router(dcf.router, prefix="/dcf-valuation", tags=["DCF Valuation"])
