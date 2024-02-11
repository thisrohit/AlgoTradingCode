import datetime as dt
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

tickers = ["INFY.NS", "MSFT", "META", "GOOG"]
start = dt.datetime.today() - dt.timedelta(5650)
end =dt.datetime.today()

cl_price = pd.DataFrame()

for ticker in tickers:
    cl_price[ticker] = yf.download(ticker, start, end)["Adj Close"]

cl_price.plot(subplots=True, layout=(2,2), title="Stock Price Evolutuin")
# plt.show()  
daily_returns = cl_price.pct_change()
daily_returns.plot(subplots=True)
# plt.show() 
df = daily_returns.rolling(window=10).mean().tail()
df.plot(subplots=True)
(1+daily_returns).cumprod().plot()
plt.show()

# df2 = daily_returns.ewm(com=10)
# print(df2)
