import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned states data
df = pd.read_csv("data/states_clean.csv", parse_dates=["date"])

# Fix: J&K and Ladakh is written in 4 different ways
df.loc[df["state"].str.contains("J&K"), "state"] = "J&K and Ladakh"

# Shortage as percent of demand for each state
summary = df.groupby("state").agg(
    days=("date", "nunique"),
    total_shortage=("shortage_mw", "sum"),
    total_demand=("max_demand_mw", "sum"),
)
summary["shortage_pct"] = summary["total_shortage"] / summary["total_demand"] * 100

# Keep only places with enough data, then take the top 8
summary = summary[summary["days"] >= 1500]
top8 = summary["shortage_pct"].sort_values(ascending=False).head(8)

# Horizontal bar chart (largest at the top)
plt.figure(figsize=(9, 6))
bars = plt.barh(top8.index[::-1], top8.values[::-1], color="firebrick")
plt.bar_label(bars, fmt="%.1f%%")
plt.title("Top 8 States by Power Shortage (% of Demand)")
plt.xlabel("Shortage as percent of demand")
plt.tight_layout()
plt.savefig("charts/shortage_states.png")
plt.show()