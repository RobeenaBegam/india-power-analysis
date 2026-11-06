import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

monthly = pd.read_csv("data/monthly.csv")

X = pd.get_dummies(monthly[["t", "month"]], columns=["month"], dtype=int)
y = monthly["avg_mu_per_day"]

test = monthly["year"] >= 2022

for start in [2013, 2015, 2017, 2019]:
    train = (monthly["year"] >= start) & (monthly["year"] <= 2021)

    model = LinearRegression()
    model.fit(X[train], y[train])

    pred = model.predict(X[test])
    mae = mean_absolute_error(y[test], pred)
    percent = mae / y[test].mean() * 100

    print("Start year:", start,
          "| Train rows:", train.sum(),
          "| Error:", round(mae, 1), "MU/day",
          "| Percent:", round(percent, 1))