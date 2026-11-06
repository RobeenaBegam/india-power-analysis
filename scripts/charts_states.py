import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned states data
df = pd.read_csv("data/states_clean.csv", parse_dates=["date"])

# Average energy met per day for each state, top 10
avg = df.groupby("state")["energy_met_mu"].mean()
top10 = avg.sort_values(ascending=False).head(10)

# Horizontal bar chart (largest at the top)
plt.figure(figsize=(9, 6))
bars = plt.barh(top10.index[::-1], top10.values[::-1], color="seagreen")
plt.bar_label(bars, fmt="%.0f")
plt.title("Top 10 States by Average Energy Met per Day")
plt.xlabel("Energy met (MU per day)")
plt.tight_layout()
plt.savefig("charts/top_states.png")
plt.show()