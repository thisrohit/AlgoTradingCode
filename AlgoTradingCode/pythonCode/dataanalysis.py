import yfinance as yf
import datetime as dt
import pandas as pd

tickers = ["AMZN", "META", "GOOG"]
start = dt.datetime.today()-dt.timedelta(365)
end = dt.datetime.today()

cl_price = pd.DataFrame()

for ticker in tickers:
    cl_price[ticker] = yf.download(ticker,start,end)["Adj Close"]

# print(cl_price)
    
cl_price.dropna(axis=0, how='any', inplace=True)
# print(cl_price)
cl_price.max()

daily_return = cl_price.pct_change()
print(daily_return)

print(daily_return.mean(axis=1))
