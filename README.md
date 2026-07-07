# risklens

Risklens is a portfolio risk and intelligence platform that helps investors assess their portfolios and spot which holdings are at risk. Right now it has a working data pipeline: it pulls data from Yahoo Finance into SQLite, and is safe to re-run without duplicating data. Next up: risk metrics - volatility, Value at Risk, and correlation. 

## Setup 

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python3 -m app.data.fetch 
```

It loads the tickers AAPL, MSFT, JPM, and SPY. The data ends up in market_data.db. It is safe to run twice as there will be no duplicates. 

## Project Structure 

- `app/data/db.py` - PriceBar class giving the format for a row. 
- `app/data/fetch.py` - Pulls the data from Yahoo Finance. 
- `DECISIONS.md` - Explains why?

## Roadmap 

- [x] Data pipeline (yfinance -> SQLite, idempotent ingestion)
- [ ] Risk metrics (volatility, VaR, correlation)
- [ ] REST API
- [ ] Anomaly detection 
- [ ] Dashboard