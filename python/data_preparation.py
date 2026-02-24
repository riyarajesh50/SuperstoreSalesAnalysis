import pandas as pd

# Load dataset
df = pd.read_csv("../data/Superstore.csv")

# Convert dates
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Create new features
df['Profit Margin'] = df['Profit'] / df['Sales']
df['Order Month'] = df['Order Date'].dt.month

# Save cleaned data
df.to_csv("../data/cleaned_superstore.csv", index=False)

print("Data cleaned and saved.")
