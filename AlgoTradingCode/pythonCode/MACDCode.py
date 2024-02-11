import yfinance as yf

tickers = ["AMZN", "GOOG", "MSFT", "TSLA", "SBIN.NS"]
ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period="1mo", interval="15m")
    temp.dropna(how='any', inplace=True)
    ohlcv_data[ticker] = temp

    
def MACD(DF, slw_ma = 26, fst_ma = 12, sgnl = 9):
    df = DF.copy()
    df["fast_ma"] = df["Adj Close"].ewm(span=fst_ma, min_periods=fst_ma).mean()
    df["slw_ma"] = df["Adj Close"].ewm(span=slw_ma, min_periods=slw_ma).mean()
    df["macd"] = df["fast_ma"] - df["slw_ma"]
    df["signal"] = df["macd"].ewm(span=sgnl, min_periods=sgnl).mean()
    return df.loc[:,["macd", "signal"]]

for ticker in tickers:
    ohlcv_data[ticker][["MACD", "SIGNAL"]] = MACD(ohlcv_data[ticker])
    
print(ohlcv_data)