import pandas as pd

# Raw data padho aur sirf Delhi lo
df = pd.read_csv("data/city_day.csv", parse_dates=["Date"])
city = df[df["City"] == "Delhi"].copy()
print("Delhi rows (raw):", city.shape[0])

# Bekaar columns hatao
city = city.drop(columns=["City", "Xylene"])
city = city.set_index("Date").sort_index()

# Pollutants ke missing values interpolate karo
num_cols = ["PM2.5", "PM10", "NO", "NO2", "NOx", "NH3",
            "CO", "SO2", "O3", "Benzene", "Toluene"]
city[num_cols] = city[num_cols].interpolate(method="time", limit_direction="both")

# Jahan AQI hi nahi hai wo rows hatao
city = city.dropna(subset=["AQI"])

print("Shape after cleaning:", city.shape)
print("Date range:", city.index.min(), "to", city.index.max())
print("Missing values:", city.isnull().sum().sum())

city.to_csv("data/delhi_clean.csv")
print("Saved: data/delhi_clean.csv")