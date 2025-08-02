from datetime import date, timedelta
from sqlalchemy.orm import Session
from app.models import InsiderTrade, AnalystRating

def detect_cluster_buys(db: Session):
    trades = db.query(InsiderTrade).filter(InsiderTrade.transaction_type == "Buy").all()
    cluster_signals = []

    # Group trades by ticker
    trades_by_ticker = {}
    for trade in trades:
        trades_by_ticker.setdefault(trade.ticker, []).append(trade)

    for ticker, trade_list in trades_by_ticker.items():
        # Sort by date
        trade_list.sort(key=lambda x: x.date)

        # Sliding window approach
        for i in range(len(trade_list)):
            window = [trade_list[i]]
            for j in range(i + 1, len(trade_list)):
                if (trade_list[j].date - trade_list[i].date).days <= 7:
                    window.append(trade_list[j])
                else:
                    break
            if len(window) >= 3:
                cluster_signals.append({
                    "ticker": ticker,
                    "num_trades": len(window),
                    "start_date": window[0].date,
                    "end_date": window[-1].date,
                    "insiders": [t.name for t in window]
                })
                break  # Only one signal per ticker
    return cluster_signals


def detect_recent_analyst_activity(db: Session):
    recent_cutoff = date.today() - timedelta(days=3)
    ratings = db.query(AnalystRating).filter(AnalystRating.date >= recent_cutoff).all()

    rating_signals = []
    for rating in ratings:
        rating_signals.append({
            "ticker": rating.ticker,
            "analyst": rating.analyst,
            "rating": rating.rating,
            "date": rating.date
        })

    return rating_signals


def generate_signals(db: Session):
    return {
        "cluster_buys": detect_cluster_buys(db),
        "recent_analyst_ratings": detect_recent_analyst_activity(db)
    }
