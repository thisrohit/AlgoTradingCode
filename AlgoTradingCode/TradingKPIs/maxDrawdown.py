import yfinance as yf
import numpy as np
import pandas as pd

tickers = ["TCS.NS", "BAJFINANCE.NS", "INFY.NS", "RELIANCE.NS", "^NSEBANK"]

ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period='120mo', interval='1d')
    temp.dropna(how='any', inplace=True)
    ohlcv_data[ticker] = temp
    
def max_dd(DF):
    df = DF.copy()
    df["return"] = df["Adj Close"].pct_change()
    df["cum_return"] = (1+df["return"]).cumprod()
    df["cum_roll_max"] = df["cum_return"].cummax()
    df["drawdown"] = df["cum_roll_max"] - df["cum_return"]
    return (df["drawdown"]/df["cum_roll_max"]).max()

for ticker in tickers:
    print("Max Drawdown of {} is {}".format(ticker, max_dd(ohlcv_data[ticker])*100))