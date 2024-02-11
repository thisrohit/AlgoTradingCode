import numpy as np
import pandas as pd

file_path = 'RELIANCE.NS.csv'
df = pd.read_csv(file_path)
print(df)

df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df = df.sort_values(by='Date')


