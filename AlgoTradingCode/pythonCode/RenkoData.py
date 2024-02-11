import yfinance as yf
import AlgoTradingCode.TradingKPIs.ATRCode as atr
from stocktrends import Renko

tickers = ["AAPL", "AMZN", "GOOG", "MSFT"]
ohlcv_data = {}
hour_data = {}
renko_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period='1mo', interval='5m')
    temp.dropna(how='any', inplace=True)
    ohlcv_data[ticker] = temp
    
    temp = yf.download(ticker, period='1y', interval='1h')
    temp.dropna(how='any', inplace=True)
    hour_data[ticker] = temp
    
def renko_DF(DF, hourly_df):
    df = DF.copy()
    df.drop("Close", axis = 1, inplace = True)
    df.reset_index(inplace = True)
    df.columns = ["date", "open", "high", "low", "close", "volumne"]
    df2 = Renko(df)
    df2.brick_size = 3*round(atr.ATR(hourly_df, 120).iloc[-1],0)
    renko_DF = df2.get_ohlc_data()
    return renko_DF

for ticker in tickers:
    renko_data[ticker] = renko_DF(ohlcv_data[ticker], hour_data[ticker])
    
for ticker in tickers:
    print(renko_data[ticker])
    
