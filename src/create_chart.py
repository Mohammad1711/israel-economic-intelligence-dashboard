import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/historical_exchange_rates.csv")

usd_df = df[df["currency_code"] == "USD"]

plt.figure(figsize=(10, 5))

plt.plot(
    usd_df["report_date"],
    usd_df["exchange_rate"],
)

plt.title("USD Exchange Rate Trend")
plt.xlabel("Date")
plt.ylabel("Exchange Rate")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("data/usd_exchange_rate_chart.png")

print("Chart created successfully.")