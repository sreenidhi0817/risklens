import yfinance as yf
from app.data.db import SessionLocal, PriceBar, init_db

def load_ticker(symbol, period="1mo"):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period)

    session = SessionLocal()

    for index, row in data.iterrows():
        exists = (
            session.query(PriceBar)
            .filter(PriceBar.ticker == symbol, PriceBar.trade_date == index.date())
            .first()
            is not None
        )
        if exists:
            continue

        bar = PriceBar(
            ticker=symbol,
            trade_date=index.date(),
            open=row["Open"],
            high=row["High"],
            low=row["Low"],
            close=row["Close"],
            volume=row["Volume"]
        )
        session.add(bar)
        
    session.commit()
    session.close()

def load_tickers(symbols):
    for symbol in symbols:
        load_ticker(symbol)

init_db()
load_tickers(["AAPL", "MSFT", "JPM", "SPY"])












