import pandas as pd
from datetime import datetime


df = pd.read_csv("data/exchange_rates.csv")

df["report_date"] = datetime.now().strftime("%Y-%m-%d")

historical_file = "data/historical_exchange_rates.csv"

try:
    historical_df = pd.read_csv(historical_file)

    updated_df = pd.concat([historical_df, df], ignore_index=True)

except FileNotFoundError:
    updated_df = df

updated_df.to_csv(historical_file, index=False)

print("Historical data updated successfully.")