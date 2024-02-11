import yfinance as yf
import datetime

def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Example: Get data for Apple Inc. from 2022-01-01 to 2023-01-01
start_date = datetime.datetime(2022, 1, 1)
end_date = datetime.datetime(2023, 1, 1)

stock_data = get_stock_data("AAPL", start_date, end_date)
print(stock_data.head())


def add_moving_averages(data, short_window=40, long_window=100):
    data['Short_MA'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    data['Long_MA'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
    return data

stock_data = add_moving_averages(stock_data)
print(stock_data.head())

def generate_signals(data):
    data['Signal'] = 0.0
    data['Signal'][data['Short_MA'] > data['Long_MA']] = 1.0  # Buy signal
    data['Signal'][data['Short_MA'] < data['Long_MA']] = -1.0  # Sell signal
    return data

stock_data = generate_signals(stock_data)
print(stock_data.head())


def backtest(data, initial_capital=10000.0):
    position = 0
    capital = initial_capital
    for index, row in data.iterrows():
        if row['Signal'] == 1.0:  # Buy
            position = capital // row['Close']
            capital = 0
        elif row['Signal'] == -1.0:  # Sell
            capital = position * row['Close']
            position = 0
    return capital + position * data['Close'].iloc[-1]

final_capital = backtest(stock_data)
print(f"Final Capital: ${final_capital:.2f}")
