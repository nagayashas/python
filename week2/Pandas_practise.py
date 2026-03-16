import pandas as pd
df = pd.read_csv("Data.csv")
# print(df.head(3))
# print(df.info())
print(df.isnull().sum())
# df = df.fillna(0)
print(df.head())