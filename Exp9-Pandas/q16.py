# 15. Read the weather.csv file and:
# Find maximum temperature
# Find minimum temperature
# Calculate average temperature
# Display records where temperature is above 35°C
# Calculate city-wise average temperature

import pandas as pd

df = pd.read_csv("weather.csv")

print("Weather Data:")
print(df)

print("\nMaximum Temperature:", df["Temperature"].max())
print("Minimum Temperature:", df["Temperature"].min())
print("Average Temperature:", df["Temperature"].mean())

print("\nRecords with temperature above 35°C:")
print(df[df["Temperature"] > 35])

print("\nCity-wise Average Temperature:")
print(df.groupby("City")["Temperature"].mean())