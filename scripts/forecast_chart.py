import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

monthly = pd.read_csv("data/monthly.csv")

X = pd.get_dummies(monthly[["t", "month"]], columns=["month"], dtype=int)
y = monthly["avg_mu_per_day"]

model = LinearRegression()
model.fit(X, y)

future = pd.DataFrame({"t": range(124, 136)})
future["month"] = [(t - 1) % 12 + 1 for t in future["t"]]
X_future = pd.get_dummies(future, columns=["month"], dtype=int)
X_future = X_future.reindex(columns=X.columns, fill_value=0)
future["predicted"] = model.predict(X_future)

monthly["fitted"] = model.predict(X)

plt.figure(figsize=(10, 5))
plt.plot(monthly["t"], monthly["avg_mu_per_day"], label="Actual", color="tab:blue")
plt.plot(monthly["t"], monthly["fitted"], label="Model fit", linestyle="--", color="gray")
plt.plot(future["t"], future["predicted"], label="Forecast (Apr 2023 - Mar 2024)", color="tab:orange", linewidth=2)
plt.xlabel("Month number (t = 4 is April 2013)")
plt.ylabel("Average generation (MU per day)")
plt.title("India power generation: actual and forecast")
plt.legend()
plt.tight_layout()
plt.savefig("charts/forecast.png")
plt.show()

print(future[["t", "predicted"]].round(0).to_string(index=False))