from yahoofinancials import YahooFinancials
import pandas as pd
import datetime as dt
import json
import tkinter as tk
from tkinter import scrolledtext

# To display data
def display_data(data):
    if isinstance(data, pd.DataFrame):
        # If the input is a Pandas DataFrame, display it using the Pandas styling options
        pd.set_option('display.max_columns', None)
        pd.set_option('display.expand_frame_repr', False)
        print(data)

    elif isinstance(data, dict) or isinstance(data, list):
        # If the input is JSON data (a dictionary or a list), pretty print it
        formatted_data = json.dumps(data, indent=2)
        print(formatted_data)

    else:
        print("Unsupported data type. Please provide a Pandas DataFrame or JSON data.")

# To display data in a new window


tickers = ["AAPL", "MSFT", "CSCO", "AMZN", "INTC"]
close_prices = pd.DataFrame()
end_date = dt.date.today().strftime('%Y-%m-%d')
start_date = (dt.date.today() - dt.timedelta(30)).strftime('%Y-%m-%d')

for ticker in tickers:
    yahoo_financials = YahooFinancials(ticker)
    json_obj = yahoo_financials.get_historical_price_data(start_date, end_date,'daily')
    ohlc_data = json_obj[ticker]['prices']
    temp = pd.DataFrame(ohlc_data)[["formatted_date", "adjclose"]]
    temp.set_index("formatted_date", inplace=True)
    temp.dropna(inplace=True)
    close_prices[ticker] = temp["adjclose"]
    display_data(close_prices[ticker])
    
