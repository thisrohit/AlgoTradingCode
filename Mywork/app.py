import pandas as pd

# Replace 'your_file_path.xlsx' with the actual path to your Excel file
file_path = 'RELIANCE.NS.csv'

# Read the Excel file into a pandas DataFrame
df = pd.read_csv(file_path)

# Display the DataFrame
# print(df)
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
# df['Date'] = pd.to_datetime(df['Date'])

# Sort the DataFrame by date in ascending order
df = df.sort_values(by='Date')

# Create a new column 'Tomorrow_Open_Greater' with True or False based on the condition
df['Tomorrow_Open_Greater'] = df['Open'].shift(-1) > df['Close']

# Count the number of days where the condition is True
num_days = df['Tomorrow_Open_Greater'].sum()

# print(f'Number of days where the opening price of tomorrow is greater than the closing price of today: {num_days}')

# Initialize variables
total_profit_loss = 0
curr_total_profit_loss = 0

# Calculate profit or loss for each day
for i in range(len(df) - 1):
    # Buy at the closing price of the current day
    buy_price = df.at[i, 'Close']
    
    # Sell at the opening price of the next day
    sell_price = df.at[i + 1, 'Open']
    
    # Calculate profit or loss for the current trade
    curr_total_profit_loss = sell_price - buy_price
    
    # Accumulate the profit or loss
    total_profit_loss += curr_total_profit_loss

# Print the total profit or loss
print(f'Total Profit/Loss: ${total_profit_loss:.2f}')

# Calculate the total number of trading days
total_days = len(df) - 1  # Since we are selling on the next day for each trade

# Calculate the average daily return
average_daily_return = total_profit_loss / total_days

# Calculate the average annual return (assuming 252 trading days in a year)
average_annual_return = average_daily_return * 252

# Print the average annual return
print(f'Average Annual Return: {average_annual_return:.2%}')

total_buyPrice = 0
avg_buyPrice = 0
# Calculate profit or loss for each day
for i in range(len(df) - 1):
    # Buy at the closing price of the current day
    buy_price = df.at[i, 'Close']
    
    total_buyPrice += buy_price
    
    
avg_buyPrice = total_buyPrice/total_days
print(avg_buyPrice)

profit = 0
profit = total_profit_loss/avg_buyPrice

print(f'Total Profit Percentage: {profit:.2%}')    

# Create a new column 'InsideRange' to store True if the price is inside the range for the last 5 days, False otherwise
# df['InsideRange'] = df['Close'].rolling(window=5).apply(lambda x: x.iloc[0] >= x.min() and x.iloc[0] <= x.max()).fillna(False)

# Print the DataFrame with the new column
# print(df[['Date', 'Close', 'InsideRange']])

# Create a new column 'InsideRange' to store True if the price is inside the range for the last 5 days, False otherwise
df['InsideRange'] = df['Close'].rolling(window=5).apply(lambda x: x.iloc[-1] >= x.min() and x.iloc[-1] <= x.max()).fillna(False)

# Filter and print only the rows where 'InsideRange' is True
filtered_df = df[df['InsideRange'] == True]  # Ensure that we are filtering only rows where 'InsideRange' is True
if not filtered_df.empty:
    print(filtered_df[['Date', 'Close']])
else:
    print("No rows found where the price was inside the range for the last 5 days.")




# Moving average testing

def add_moving_averages(data, short_window=40, long_window=100):
    data['Short_MA'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    data['Long_MA'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
    return data

stock_data = add_moving_averages(df)
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

