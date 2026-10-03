import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset/ai4i2020.csv")

df["Machine failure"].value_counts().plot(kind="bar")

plt.title("Machine Failure Distribution")

plt.show()