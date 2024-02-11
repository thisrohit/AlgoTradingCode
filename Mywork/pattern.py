import yfinance as yf
import pandas as pd

def calculate_trendlines(stock_data):
    # Find the highest and lowest points within the flag
    highest_point = stock_data['High'].max()
    highest_index = stock_data['High'].idxmax()
    lowest_point = stock_data['Low'].min()
    lowest_index = stock_data['Low'].idxmin()

    # Calculate the slope of the trendline passing through the highest and lowest points
    slope = (highest_point - lowest_point) / (highest_index - lowest_index)

    # Calculate the y-intercept of the trendline
    y_intercept = highest_point - slope * highest_index

    return slope, y_intercept



def identify_flag_pattern(stock_data):
    # Identify a sharp initial move (flagpole)
    flagpole_start_index = None
    flagpole_end_index = None
    for i in range(len(stock_data)):
        if stock_data['Close'][i] > stock_data['Close'][0]:
            flagpole_start_index = i
            break

    if flagpole_start_index is None:
        return None

    for i in range(flagpole_start_index, len(stock_data)):
        if stock_data['Close'][i] <= stock_data['Close'][flagpole_start_index]:
            flagpole_end_index = i
            break

    if flagpole_end_index is None:
        return None

    flagpole_length = flagpole_end_index - flagpole_start_index

    # Identify a consolidation phase (flag)
    flag_start_index = flagpole_end_index
    flag_end_index = None
    upper_trendline_slope, lower_trendline_slope = calculate_trendlines(stock_data[flag_start_index:])

    for i in range(flag_start_index + flagpole_length, len(stock_data)):
        if (stock_data['Close'][i] >= upper_trendline_slope * (i - flag_start_index) + stock_data['Close'][flag_start_index]) and (
                stock_data['Close'][i] <= lower_trendline_slope * (i - flag_start_index) + stock_data['Close'][flag_start_index]):
            flag_end_index = i
            break

    if flag_end_index is None:
        return None

    # Check for a breakout
    if stock_data['Close'][flag_end_index] > upper_trendline_slope * (flag_end_index - flag_start_index) + stock_data['Close'][flag_start_index]:
        return "Bullish Flag"
    elif stock_data['Close'][flag_end_index] < lower_trendline_slope * (flag_end_index - flag_start_index) + stock_data['Close'][flag_start_index]:
        return "Bearish Flag"
    else:
        return None



# Define the Nifty 500 index
nifty500 = yf.index.nifty500()

# Get historical data for each stock in Nifty 500
historical_data = {}
for stock_ticker in nifty500.constituents:
    stock_data = yf.download(stock_ticker, period="max")
    historical_data[stock_ticker] = stock_data

# Initialize an empty list to store stocks with identified patterns
stocks_with_patterns = []

# Analyze each stock for flag, pennant, and triangle patterns
for stock_ticker, stock_data in historical_data.items():
    # Identify flag patterns
    flag_pattern = identify_flag_pattern(stock_data)
    if flag_pattern:
        stocks_with_patterns.append((stock_ticker, flag_pattern))

    # # Identify pennant patterns
    # pennant_pattern = identify_pennant_pattern(stock_data)
    # if pennant_pattern:
    #     stocks_with_patterns.append((stock_ticker, pennant_pattern))

    # # Identify triangle patterns
    # triangle_pattern = identify_triangle_pattern(stock_data)
    # if triangle_pattern:
    #     stocks_with_patterns.append((stock_ticker, triangle_pattern))

# Extract stock names and corresponding patterns
stock_names_and_patterns = []
for stock_ticker, pattern in stocks_with_patterns:
    stock_name = nifty500.get_stock_info(stock_ticker).company_name
    stock_names_and_patterns.append((stock_name, pattern))

# Print the list of stock names and corresponding patterns
for stock_name, pattern in stock_names_and_patterns:
    print(f"Stock: {stock_name}")
    print(f"Pattern: {pattern}")
    

