import pandas as pd

# 1. Load both files
source = pd.read_csv("data/power_source.csv")
states = pd.read_csv("data/power_states.csv")

# 2. Convert date text into real dates
source["date"] = pd.to_datetime(source["date"])
states["date"] = pd.to_datetime(states["date"])

# 3. Simple column names
source.columns = ["source", "nr", "wr", "sr", "er", "ner", "all_india", "date"]
states.columns = ["region", "state", "max_demand_mw", "shortage_mw", "energy_met_mu", "date"]

# 4. Remove rows with missing values
print("States rows before:", len(states))
states = states.dropna()
print("States rows after:", len(states))

# 5. Save the clean files
source.to_csv("data/source_clean.csv", index=False)
states.to_csv("data/states_clean.csv", index=False)

# Check
print()
print(source.dtypes)
print()
print(states.dtypes)
print()
print(states.isnull().sum())