from app.data.db import init_db
from app.data.fetch import load_tickers

if __name__ == "__main__":
    init_db()
    load_tickers(["AAPL", "MSFT", "JPM", "SPY"])



