# csv_analyzer.py
import pandas as pd
df = pd.read_csv("data.csv")
print(df.describe())
print("Null Values:\n", df.isnull().sum())
