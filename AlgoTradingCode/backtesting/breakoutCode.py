import yfinance as yf
import numpy as np
import copy
import pandas as pd
        
def ATR(DF, n):
    df = DF.copy()
    df["H-L"] = df["High"] - df["Low"]
    df["H-PC"] = df["High"] - df["Close"].shift(1)
    df["L-PC"] = df["Low"] - df["Close"].shift(1)
    df["TR"] = df[["H-L", "H-PC", "L-PC"]].max(axis=1, skipna = False)
    df["ATR"] = df["TR"].ewm(com=n, min_periods=n).mean()    
    df2 = df.drop(['H-L', 'H-PC', 'L-PC'], axis=1)
    return df2["ATR"]

def CAGR(DF):
    df = DF.copy()
    df["Returns"] = df["Adj Close"].pct_change()
    df["Cum_returns"] = (1+df["Returns"]).cumprod()
    n = len(df)/(252*78)
    CAGR = (df["Cum_returns"][-1])**(1/n) - 1
    return CAGR

def volatility(DF):
    df = DF.copy()
    df["return"] = df["Adj Close"].pct_change()
    vola = df["return"].std() * np.sqrt(252*78)
    return vola

def max_dd(DF):
    df = DF.copy()
    df["return"] = df["Adj Close"].pct_change()
    df["cum_return"] = (1+df["return"]).cumprod()
    df["cum_roll_max"] = df["cum_return"].cummax()
    df["drawdown"] = df["cum_roll_max"] - df["cum_return"]
    df["drawdwn_pct"] = df["drawdown"]/df["cum_roll_max"]
    max_drawdown = df["drawdwn_pct"].max()
    return max_drawdown

tickers = [
    "HDFCBANK.NS",
    # "ICICIBANK.NS",
    # "SBIN.NS",
    # "AXISBANK.NS",
    # "KOTAKBANK.NS",
    # "BAJAJFINSV.NS",
    # "INDUSINDBK.NS",
    "BANKBARODA.NS",
    # "AUBANK.NS",
    # "FEDERALBNK.NS",
    # "PNB.NS",
    # "IDFCFIRSTB.NS",
    # "CANBK.NS",
    # "UNIONBANK.NS",
    # "HDFCLIFE.NS",
    # "ICICIGI.NS",
    "SBILIFE.NS",
]

ohlcv_intraday = {}

for ticker in tickers:
    temp = yf.download(ticker, period="1mo", interval='5m')
    temp.dropna(inplace=True, how='any')
    ohlcv_intraday[ticker] = temp
    
tickers = ohlcv_intraday.keys()

#calculating the ATR rolling_max_cp min_cp Volume 
ohlc_dict = copy.deepcopy(ohlcv_intraday)
ticker_signal = {}
ticker_ret = {}

for ticker in tickers:
    ohlc_dict[ticker]["ATR"] = ATR(ohlc_dict[ticker], 20)
    ohlc_dict[ticker]["roll_max_cp"] = ohlc_dict[ticker]["High"].rolling(20).max()
    ohlc_dict[ticker]["roll_min_cp"] = ohlc_dict[ticker]["Low"].rolling(20).min()
    ohlc_dict[ticker]["roll_max_vol"] = ohlc_dict[ticker]["Volume"].rolling(20).max()
    ohlc_dict[ticker].dropna(inplace=True)
    ticker_signal[ticker] = ""
    ticker_ret[ticker] = [0]
    # print(ohlc_dict[ticker].keys())
    
#signals for buy and sell

for ticker in tickers:
    for i in range(1, len(ohlc_dict[ticker])):
        if ticker_signal[ticker] == "":
            ticker_ret[ticker].append(0)
            if ohlc_dict[ticker]["High"].iloc[i] >= ohlc_dict[ticker]["roll_max_cp"].iloc[i] \
                and ohlc_dict[ticker]["Volume"].iloc[i] > 1.4*ohlc_dict[ticker]["roll_max_vol"].iloc[i-1]:
                    ticker_signal[ticker] = "Buy"
            elif ohlc_dict[ticker]["Low"].iloc[i] >= ohlc_dict[ticker]["roll_min_cp"].iloc[i] \
                and ohlc_dict[ticker]["Volume"].iloc[i] > 1.4*ohlc_dict[ticker]["roll_max_vol"].iloc[i-1]:
                    ticker_signal[ticker] = "Sell"
        
        elif ticker_signal[ticker] == "Buy":
            # closing position due to SL or reversal
            if ohlc_dict[ticker]["Low"] < (ohlc_dict[ticker]["Close"].iloc[i-1] - ohlc_dict[ticker]["ATR"].iloc[i-1]):
                ticker_signal = ""
                ticker_ret[ticker].append((ohlc_dict[ticker]["Close"].iloc[i-1] - ohlc_dict[ticker]["ATR"].iloc[i-1])/ohlc_dict[ticker]["Close"] - 1)
            elif ohlc_dict[ticker]["Low"] <= ohlc_dict[ticker]["roll_min_cp"].iloc[i-1] \
                and ohlc_dict[ticker]["Volume"] >= 1.4* ohlc_dict[ticker]["roll_max_cp"]:
                    ticker_signal = "Sell"
                    ticker_ret[ticker].append(ohlc_dict[ticker]["Close"].iloc[i]/ohlc_dict[ticker]["Close"].iloc[i-1] - 1)
            else:
                    ticker_ret[ticker].append(ohlc_dict[ticker]["Close"].iloc[i]/ohlc_dict[ticker]["Close"].iloc[i-1] - 1)
        
        elif ticker_signal[ticker] == "Sell":
            if ohlc_dict[ticker]["High"].iloc[i] > ohlc_dict[ticker]["Close"].iloc[i-1] + ohlc_dict[ticker]["ATR"].iloc[i-1]:
                ticker_signal = ""
                ticker_ret[ticker].append(ohlc_dict[ticker]["Close"].iloc[i-1]/(ohlc_dict[ticker]["Close"].iloc[i-1] - ohlc_dict[ticker]["ATR"].iloc[i-1]) - 1)
            
            elif ohlc_dict[ticker]["High"].iloc[i] >= ohlc_dict[ticker]["roll_max_cp"].iloc[i-1] \
                and ohlc_dict[ticker]["Volume"].iloc[i] >= 1.4* ohlc_dict[ticker]["roll_max_Volume"]:
                    ticker_signal = "Buy"
                    ticker_ret[ticker].append(ohlc_dict[ticker]["Close"].iloc[i]/ohlc_dict[ticker]["Close".iloc[i-1]] - 1)
                    
            else:
                ticker_ret[ticker].append(ohlc_dict[ticker]["Close"].iloc[i]/ohlc_dict[ticker]["Close".iloc[i-1]] - 1)
        
    ohlc_dict[ticker]["ret"] = np.array(ticker_ret[ticker])
    
strategy_df = pd.DataFrame()    

for ticker in tickers:
    strategy_df[tickers] = ohlc_dict[tickers]["res"]
    
print(CAGR(strategy_df))
    