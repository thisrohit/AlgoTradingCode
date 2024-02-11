import yfinance as yf

tickers = ["AAPL", "MSFT", "AMZN", "META", "SBIN.NS"]

ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period="1mo", interval="5m")
    temp.dropna(how='any', inplace=True)
    ohlcv_data[ticker] = temp
    
def BolBand(DF, n=14):
    df = DF.copy()
    df["MB"] = df["Adj Close"].rolling(n).mean()
    df["UB"] = df["MB"] + 2*df["Adj Close"].rolling(n).std(ddof=0)
    df["LB"] = df["MB"] - 2*df["Adj Close"].rolling(n).std(ddof=0)
    df["BB_width"] = df["UB"] - df["LB"]
    return df[["MB", "UB", "LB", "BB_width"]]

for ticker in tickers:
    ohlcv_data[ticker][["MB", "UB", "LB", "BB_width"]] = BolBand(ohlcv_data[ticker], 20)
    
for ticker in tickers:
    print(ticker)
    print(ohlcv_data[ticker])