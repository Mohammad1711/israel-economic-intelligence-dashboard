import requests
import pandas as pd
import xml.etree.ElementTree as ET


url = "https://boi.org.il/PublicApi/GetExchangeRates?asXml=true"

response = requests.get(url)

root = ET.fromstring(response.content)

namespace = {'ns': 'http://schemas.datacontract.org/2004/07/BOI.Core.Models.HotData'}

rows = []

for item in root.findall(".//ns:ExchangeRateResponseDTO", namespace):

    rows.append({
        "currency_code": item.findtext("ns:Key", default="", namespaces=namespace),
        "exchange_rate": item.findtext("ns:CurrentExchangeRate", default="", namespaces=namespace),
        "change": item.findtext("ns:CurrentChange", default="", namespaces=namespace),
        "unit": item.findtext("ns:Unit", default="", namespaces=namespace),
        "last_update": item.findtext("ns:LastUpdate", default="", namespaces=namespace),
    })

df = pd.DataFrame(rows)

df["exchange_rate"] = pd.to_numeric(df["exchange_rate"], errors="coerce")
df["change"] = pd.to_numeric(df["change"], errors="coerce")

print(df.head())

df.to_csv("data/exchange_rates.csv", index=False)

print("CSV file saved successfully.")