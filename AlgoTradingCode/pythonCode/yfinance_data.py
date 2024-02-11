import yfinance as yf
import os
import datetime as dt
import pandas as pd

# data = yf.download("MSFT", period="1mo", interval="15m")
# data.to_csv("msft_data.csv")
# print(data)

def create_DataCSV(ticker):
    folder_path = "AlgoTradingCourse/data"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = os.path.join(folder_path, "msft_data.csv")
    data = yf.download(ticker, period="1mo", interval="15m")
    data.to_csv(file_path)
    
stocks = ["AMZN", "MSFT", "INTC", "INFY.NS", "3988.HK"]
start_data = dt.datetime.today() - dt.timedelta(30)
end_date = dt.datetime.today()

cls_price = pd.DataFrame()
ohclv_data = {}

for ticker in stocks:
    cls_price[ticker] = yf.download(ticker, start_data, end_date)["Adj Close"]

# cls_price.to_csv("Adj_Close_data")
# print(cls_price)

for ticker in stocks:
    ohclv_data[ticker] = yf.download(ticker, start_data, end_date)

print(ohclv_data)    


    

    
