import pandas as pd

# Load the cleaned states data
df = pd.read_csv("data/states_clean.csv", parse_dates=["date"])

# Fix: J&K and Ladakh is written in 4 different ways
df.loc[df["state"].str.contains("J&K"), "state"] = "J&K and Ladakh"

# Summary for each state
summary = df.groupby("state").agg(
    days=("date", "nunique"),
    avg_shortage_mw=("shortage_mw", "mean"),
    total_shortage=("shortage_mw", "sum"),
    total_demand=("max_demand_mw", "sum"),
)
summary["shortage_pct"] = summary["total_shortage"] / summary["total_demand"] * 100

# Keep only places with enough data (removes Railways, BALCO, etc.)
summary = summary[summary["days"] >= 1500]
print("Places kept:", len(summary))
print()

print("Top 8 by average shortage (MW):")
print(summary.sort_values("avg_shortage_mw", ascending=False).head(8)[["days", "avg_shortage_mw"]].round(1))
print()

print("Top 8 by shortage as percent of demand:")
print(summary.sort_values("shortage_pct", ascending=False).head(8)[["days", "shortage_pct"]].round(2))