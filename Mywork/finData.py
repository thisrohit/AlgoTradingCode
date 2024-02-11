import yfinance as yf
import pandas as pd
import subprocess

def get_historical_data(symbol, start_date, end_date):
    # Fetch historical data from Yahoo Finance
    stock_data = yf.download(symbol, start=start_date, end=end_date)

    # Save the data to a CSV file
    csv_file_path = f'{symbol}_historical_data.csv'
    stock_data.to_csv(csv_file_path)

    print(f'Historical data for {symbol} saved to {csv_file_path}')
    
    # Automatically open the file using the default CSV viewer
    try:
        subprocess.run(['open', csv_file_path], check=True)
    except Exception as e:
        print(f'Error opening the file: {e}')

# Example usage:
symbol = 'AAPL'  # Replace with the desired stock symbol
start_date = '2022-01-01'  # Replace with the desired start date
end_date = '2023-01-01'    # Replace with the desired end date

get_historical_data(symbol, start_date, end_date)
