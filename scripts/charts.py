import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned source data and keep only the Total rows
df = pd.read_csv("data/source_clean.csv", parse_dates=["date"])
df = df[df["source"].str.contains("Total")]

# ---------- Chart 1: yearly average generation per day ----------
yearly = df.groupby(df["date"].dt.year)["all_india"].mean()

plt.figure(figsize=(9, 5))
plt.plot(yearly.index, yearly.values, marker="o", color="green")
plt.title("India: Average Power Generation per Day")
plt.xlabel("Year")
plt.ylabel("Generation (MU per day)")
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/yearly_generation.png")

# ---------- Chart 2: share of generation by region ----------
regions = ["nr", "wr", "sr", "er", "ner"]
totals = df[regions].sum()
share = totals / totals.sum() * 100
share.index = ["North", "West", "South", "East", "North-East"]

plt.figure(figsize=(9, 5))
bars = plt.bar(share.index, share.values, color="steelblue")
plt.bar_label(bars, fmt="%.1f%%")
plt.title("Share of India's Power Generation by Region")
plt.ylabel("Share (%)")
plt.tight_layout()
plt.savefig("charts/region_share.png")

plt.show()