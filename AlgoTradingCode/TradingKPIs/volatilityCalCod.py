import yfinance as yf
import numpy as np

tickers = ["AAPL", "AMZN", "MSFT", "INFY.NS", "RELIANCE.NS", "^NSEBANK"]

ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period='1mo', interval='1h')
    temp.dropna(how='any', inplace=True)
    ohlcv_data[ticker] = temp
    
def volatility(DF):
    df = DF.copy()
    df["return"] = df["Adj Close"].pct_change()
    vola = df["return"].std() * np.sqrt(252)
    return vola
    
for ticker in tickers:
    print("Volatility for {} is  {}".format(ticker, volatility(ohlcv_data[ticker])))