import pandas as pd

df = pd.read_csv("Dataset/ai4i2020.csv")

print(df.isnull().sum())