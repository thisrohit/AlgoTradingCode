import yfinance as yf

tickers =["INFY.NS", "RELIANCE.NS"]

for ticker in tickers:
    temp = yf.download(ticker, period="1d", interval='15m')
    