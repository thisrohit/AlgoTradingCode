# Sarte Ratio - Avg return earned in excess of the risk free rate per unit of volatility
    #widely used in risk adjusted return
    #sharpe ratio > 1 Good, > 2 Very Good, > 3 Excellent
    # Sharpe Ratio = (Rp - Rf)/sigmap 
        #Rp - Excepted return, Rf - Risk free rate of return, sigma - SD of asset
        
# Sortino Ratio - Variation of Sharpe ratio which considers SD of negative return only
    # Sortino Ratio = (Rp - Rf)/sigmap 
        #Rp - Excepted return, Rf - Risk free rate of return, 
        # sigma - SD of negative asset returns
        
import yfinance as yf
import numpy as np
import pandas as pd

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

def CAGR(DF):
    df = DF.copy()
    df["Returns"] = df["Adj Close"].pct_change()
    df["Cum_returns"] = (1+df["Returns"]).cumprod()
    n = len(df)/252
    CAGR = (df["Cum_returns"][-1])**(1/n) - 1
    return CAGR

def sharpe(DF, rf):
    df = DF.copy()
    return (CAGR(df) - rf)/volatility(df)

def sortino(DF, rf):
    df = DF.copy()
    df["returns"] = df.pct_change()
    neg_return = np.where(df["return"] > 0, 0, df["return"])
    neg_vola = pd.Series(neg_return[neg_return != 0]).std() * np.sqrt(252)
    return (CAGR(df) - rf)/neg_vola

for ticker in tickers:
    print("Sharpe for {} is {}".format(ticker, sharpe(ohlcv_data[ticker], 0.03)))
    print("Sortino for {} is {}".format(ticker, sortino(ohlcv_data[ticker], 0.03)))
    