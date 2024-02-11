from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import time

key_path = "D:\my Work\documents\AlphaVantage_APIKey.txt"

all_tickers = ["INFY.NS", "MSFT", "CSCO", "AMZN", "GOOG", "FB"]
close_prices = pd.DataFrame()
api_calls_count = 0

for ticker in all_tickers:
    starttime = time.time()
    
    # Move the TimeSeries instance outside of the loop to avoid unnecessary API key reads
    ts = TimeSeries(key=open(key_path, 'r').read(), output_format='pandas')
    
    try:
        data, meta_data = ts.get_intraday(symbol=ticker, interval='5min', outputsize='compact')
        api_calls_count += 1
        data.columns = ["open", "high", "low", "close", "volume"]
        close_prices[ticker] = data["close"]

        if api_calls_count == 5:
            api_calls_count = 0
            time.sleep(60 - (time.time() - starttime) % 60.0)
    
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")

# Print or use close_prices DataFrame as needed
print(close_prices)
