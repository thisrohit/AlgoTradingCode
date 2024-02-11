import MetaTrader5 as mt5
import os
import datetime as dt
import pandas as pd

os.chdir(r"D:\my Work\AutomatedTradingCode\key")
key = open("keymt5.txt","r").read().split()
path = r"C:\Users\584851\AppData\Roaming\MetaTrader 5\terminal64.exe"

#creating connection
if mt5.initialize(path=path, login = int(key[0]), password = key[1], server=key[2]):
    print("Connection Established")
else:
    print("Failed")
    
#fetching historical data
hist_data = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_M15, dt.datetime(2023, 10, 1), 200)
hist_data_df = pd.DataFrame(hist_data)
# print(hist_data)
hist_data_df.time = pd.to_datetime(hist_data_df.time, unit='s')
hist_data_df.set_index("time", inplace=True)
print(hist_data_df)

