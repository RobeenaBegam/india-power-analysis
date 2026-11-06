import pandas as pd

df = pd.read_csv("data/source_clean.csv", parse_dates=["date"])

total = df[df["source"] == "Total"].copy()
total["year"] = total["date"].dt.year
total["month"] = total["date"].dt.month

monthly = total.groupby(["year", "month"]).agg(
    avg_mu_per_day=("all_india", "mean"),
    days=("all_india", "count"),
).reset_index()

monthly = monthly[monthly["days"] >= 20].copy()
monthly["t"] = (monthly["year"] - 2013) * 12 + monthly["month"]

monthly.to_csv("data/monthly.csv", index=False)

print(monthly.head())
print(monthly.tail())
print("Rows:", len(monthly))