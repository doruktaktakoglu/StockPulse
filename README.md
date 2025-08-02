# 📊 StockPulse

> **Advanced Stock Signal Analysis Platform** - Track insider trading patterns, analyst ratings, and DCF valuations in real-time

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4.0-red?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://sqlalchemy.org/)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org/)

---

## 🚀 Features

### 📈 **Insider Trading Analysis**
- **Cluster Buy Detection**: Identifies when 3+ insiders buy the same stock within 7 days
- **Real-time Data**: Scrapes insider trading data from OpenInsider
- **Pattern Recognition**: Analyzes trading patterns for investment signals

### 🎯 **Analyst Rating Tracking**
- **Finnhub Integration**: Fetches real-time analyst ratings and recommendations
- **Recent Activity Monitoring**: Tracks analyst activity within the last 3 days
- **Rating Aggregation**: Consolidates multiple analyst opinions

### 💰 **DCF Valuation Analysis**
- **Multi-Source Data**: Scrapes DCF valuations from AlphaSpread and ValueInvesting
- **Comparative Analysis**: Compares valuations across different sources
- **Ticker-Specific**: Get detailed DCF analysis for any stock ticker

### 🔍 **Smart Signal Generation**
- **Automated Detection**: Identifies high-probability investment opportunities
- **Risk Assessment**: Analyzes insider confidence and analyst sentiment
- **API-First Design**: RESTful endpoints for easy integration

---

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Data Sources**: Finnhub API, OpenInsider, AlphaSpread, ValueInvesting
- **Architecture**: Modular router-based design
- **Documentation**: Auto-generated OpenAPI/Swagger docs

---

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/StockSignalAnalysis.git
cd StockSignalAnalysis/insider_analyst_tracker

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
export FINNHUB_API_KEY="your_finnhub_api_key_here"

# Initialize the database
python -c "from app.database import init_db; init_db()"
```

---

## 🚀 Quick Start

### 1. Start the API Server
```bash
uvicorn app.main:app --reload
```

### 2. Access the API
- **API Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

### 3. Ingest Sample Data
```bash
python real_ingest.py
```

---

## 🚀 API Endpoints

### 🚀 **Signals Analysis**
```http
GET /signals/
```
Returns generated investment signals including cluster buys and recent analyst activity.

### 📊 **Insider Trades**
```http
GET /insider-trades/all
```
Retrieves all insider trading data from the database.

### 🎯 **Analyst Ratings**
```http
GET /analyst-ratings/
```
Fetches recent analyst ratings and recommendations.

### 💰 **DCF Valuations**
```http
GET /dcf-valuation/{ticker}
```
Gets DCF valuation data for a specific ticker from multiple sources.

---

## 🚀 Configuration

### Environment Variables
```bash
FINNHUB_API_KEY=your_finnhub_api_key_here
```

### Database
- **Type**: SQLite
- **File**: `tracker.db`
- **Auto-initialization**: Database tables created on startup

---

## 📊 Data Models

### Insider Trade
```python
{
    "ticker": "AAPL",
    "name": "Tim Cook",
    "role": "CEO",
    "date": "2024-01-15",
    "transaction_type": "Buy",
    "shares": 1000,
    "value": 150000.00
}
```

### Analyst Rating
```python
{
    "ticker": "AAPL",
    "analyst": "Morgan Stanley",
    "rating": "Overweight",
    "date": "2024-01-15"
}
```

### DCF Valuation
```python
{
    "ticker": "AAPL",
    "source": "alphaspread",
    "value": 185.50,
    "date": "2024-01-15"
}
```

---

## 🚀 Use Cases

### For Individual Investors
- **Signal Detection**: Identify high-probability investment opportunities
- **Risk Management**: Understand insider confidence levels
- **Market Timing**: Track analyst sentiment changes

### For Quantitative Analysts
- **Data Integration**: Access structured financial data via API
- **Backtesting**: Historical signal analysis capabilities
- **Custom Analysis**: Extend with additional data sources

### For Financial Institutions
- **Portfolio Management**: Incorporate insider and analyst signals
- **Risk Assessment**: Monitor insider trading patterns
- **Compliance**: Track regulatory compliance requirements

---

## 🔍 Signal Types

### 🚀 **Cluster Buy Signals**
- **Trigger**: 3+ insiders buy same stock within 7 days
- **Confidence**: High (insider knowledge)
- **Timeframe**: Short to medium term

### 🎯 **Analyst Activity Signals**
- **Trigger**: Recent analyst rating changes
- **Confidence**: Medium (professional analysis)
- **Timeframe**: Medium term

### 💰 **DCF Valuation Signals**
- **Trigger**: Significant valuation discrepancies
- **Confidence**: Medium (fundamental analysis)
- **Timeframe**: Long term

---

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup
```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests (if available)
python -m pytest

# Format code
black .
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🚀 Acknowledgments

- **Finnhub** for providing analyst rating data
- **OpenInsider** for insider trading information
- **AlphaSpread** and **ValueInvesting** for DCF valuations
- **FastAPI** team for the excellent web framework

---

