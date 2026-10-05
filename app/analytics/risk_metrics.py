import pandas as pd
from app.data.db import engine
import math

def load_prices(ticker):
    query = f"SELECT * FROM price_bars WHERE ticker = '{ticker}'"
    df = pd.read_sql(query, engine)
    return df

def add_daily_returns(df):
    df["daily_return"] = df["close"].pct_change()
    return df

def calculate_volatility(df):
    volatility = df["daily_return"].std() * math.sqrt(252)
    return volatility

def calculate_correlation(tickers):
    returns = {}
    for ticker in tickers:
        df = load_prices(ticker)
        df = add_daily_returns(df)
        returns[ticker] = df["daily_return"]
    returns_df = pd.DataFrame(returns)
    return returns_df.corr()

def calculate_value_at_risk(df):
    value_at_risk = df["daily_return"].dropna().quantile(0.05)
    return value_at_risk
