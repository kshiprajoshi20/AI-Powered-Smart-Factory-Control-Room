import pandas as pd
import pickle

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load Dataset
df = pd.read_csv("Dataset/ai4i2020.csv")

# Remove unnecessary columns
df = df.drop(["UDI", "Product ID"], axis=1)

# Convert Type column
le = LabelEncoder()
df["Type"] = le.fit_transform(df["Type"])

# Inputs and Output
X = df.drop("Machine failure", axis=1)
y = df["Machine failure"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("models/model.pkl", "wb"))

print("Model Saved Successfully")