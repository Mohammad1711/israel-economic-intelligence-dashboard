import pandas as pd


df = pd.read_csv("data/exchange_rates.csv")

print("=== Exchange Rate Summary ===")

print("\nHighest exchange rate:")
highest = df.loc[df["exchange_rate"].idxmax()]
print(highest)

print("\nLowest exchange rate:")
lowest = df.loc[df["exchange_rate"].idxmin()]
print(lowest)

print("\nAverage exchange rate:")
print(df["exchange_rate"].mean())

print("\nTop 5 strongest changes:")
top_changes = df.sort_values(by="change", ascending=False)
print(top_changes[["currency_code", "change"]].head())

print("\nTop 5 weakest changes:")
weak_changes = df.sort_values(by="change")
print(weak_changes[["currency_code", "change"]].head())