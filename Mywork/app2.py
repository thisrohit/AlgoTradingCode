import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv('RELIANCE.NS.csv')  # Replace 'your_dataset.csv' with your actual file path

# Assume you have a 'Close' column as your target variable

# Feature engineering (you may need to add more features based on your dataset)
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y');
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Select features and target variable
features = ['Day_of_Week', 'Day_of_Month', 'Month', 'Year']
X = df[features]
y = df['Close']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Plot actual vs predicted values
plt.scatter(X_test['Date'], y_test, color='black', label='Actual')
plt.scatter(X_test['Date'], y_pred, color='blue', label='Predicted')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()
