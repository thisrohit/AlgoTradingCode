import yfinance as yf

tickers = ["AMZN", "GOOG", "MSFT"]
ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period='12mo', interval='1d')
    temp.dropna(how='any', inplace=True)
    ohlcv_data[ticker] = temp
    
def CAGR(DF):
    df = DF.copy()
    df["Returns"] = df["Adj Close"].pct_change()
    df["Cum_returns"] = (1+df["Returns"]).cumprod()
    n = len(df)/252
    CAGR = (df["Cum_returns"][-1])**(1/n) - 1
    return CAGR

for ticker in tickers:
    print("CAGR for {} = {}".format(ticker, CAGR(ohlcv_data[ticker])))
    
    