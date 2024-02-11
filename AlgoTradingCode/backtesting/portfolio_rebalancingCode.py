import yfinance as yf
import numpy as np
import datetime as dt
import copy
import pandas as pd

#calcuating the cumulative annual return
def CAGR(DF):
    df = DF.copy()
    df["cum_returns"] = (1+df["mon_return"]).cumprod()
    n = len(df)/12
    CAGR = (df["cum_returns"].tolist()[-1])**(1/n) - 1
    return CAGR

def volatility(DF):
    df = DF.copy()
    vola = df["mon_return"].std() * np.sqrt(12)
    return vola

def sharpe(DF, rf):
    df = DF.copy()
    return (CAGR(df) - rf)/volatility(df)

def sortino(DF, rf):
    df = DF.copy()
    df["returns"] = df.pct_change()
    neg_return = np.where(df["return"] > 0, 0, df["return"])
    neg_vola = pd.Series(neg_return[neg_return != 0]).std() * np.sqrt(252)
    return (CAGR(df) - rf)/neg_vola

def max_dd(DF):
    df = DF.copy()
    df["cum_return"] = (1+df["mon_return"]).cumprod()
    df["cum_roll_max"] = df["cum_return"].cummax()
    df["drawdown"] = df["cum_roll_max"] - df["cum_return"]
    df["drawdown_pct"] = df["drawdown"]/df["cum_return"]
    max_dd = df["drawdown_pct"].max()
    return max_dd

#fetching historical data to backtest my strategy

tickers = [
    "HDFCBANK.NS",
    "ICICIBANK.NS",
    "SBIN.NS",
    "AXISBANK.NS",
    "KOTAKBANK.NS",
    "BAJAJFINSV.NS",
    "INDUSINDBK.NS",
    "BANKBARODA.NS",
    "AUBANK.NS",
    "FEDERALBNK.NS",
    "PNB.NS",
    "IDFCFIRSTB.NS",
    "CANBK.NS",
    "UNIONBANK.NS",
    "HDFCLIFE.NS",
    "ICICIGI.NS",
    "SBILIFE.NS",
]

#to get ohlc data for each stock
ohlc_mon = {}
start = dt.datetime.today() - dt.timedelta(3650)
end = dt.datetime.today()

#looping over the tickers and getting close price for all
for ticker in tickers:
    ohlc_mon[ticker] = yf.download(ticker, start, end, interval='1mo')
    ohlc_mon[ticker].dropna(how='all', inplace = True)
    
tickers = ohlc_mon.keys() #redefing tickers removing any corrupt values


##### Backtesting ####
#calculating monthly return for each stock and consolidating return info
ohlc_dict = copy.deepcopy(ohlc_mon)
returns_df = pd.DataFrame()
for ticker in tickers:
    print("calculating monthly return for ",ticker)
    ohlc_dict[ticker]["mon_return"] = ohlc_dict[ticker]["Adj Close"].pct_change()
    returns_df[ticker] = ohlc_dict[ticker]["mon_return"]
    
returns_df.dropna()


#function to calculate the portfolio return, m - no. of stocks at any time
# x - no. of stocks that we will rebalance
def pflio_ret(DF, m, x):
    df = DF.copy()
    portfolio = []
    monthly_ret = [0]
    
    for i in range (len(df)):
        if len(portfolio) > 0:
            monthly_ret.append(df[portfolio].iloc[i,:].mean())
            bad_stocks = df[portfolio].iloc[i,:].sort_values(ascending=True)[:x].index.values.tolist()
            portfolio = [t for t in portfolio if t not in bad_stocks]
        fill = m - len(portfolio)
        new_picks = df.iloc[i,:].sort_values(ascending=False)[:fill].index.values.tolist()
        portfolio = portfolio + new_picks
        print(portfolio)
        
    monthly_ret_df = pd.DataFrame(np.array(monthly_ret), columns=["mon_return"])
    return monthly_ret_df

#calcualting overall strategy's KPIs

print(CAGR(pflio_ret(returns_df, 6, 5)))
# print(sharpe(pflio_ret(returns_df, 6, 3),.03))
# print(max_dd(pflio_ret(returns_df, 6, 3)))

#calculatin for bnf return

bnf = yf.download("^NSEBANK", start, end, interval='1mo')
bnf["mon_return"] = bnf["Adj Close"].pct_change().fillna(0)
bnf_return = CAGR(bnf)

print("Bank Nifty annual return for same", bnf_return)



    