import pandas as pd
import matplotlib.pyplot as plt

ORANGE = "#C97A2B"
DARK = "#1F2933"

# Create the dataframe directly
data = [
    ["EU Average", 2015, "Male", 37.84],
    ["EU Average", 2015, "Female", 32.60],
    ["EU Average", 2016, "Male", 38.05],
    ["EU Average", 2016, "Female", 32.83],
    ["EU Average", 2017, "Male", 38.34],
    ["EU Average", 2017, "Female", 33.23],
    ["EU Average", 2018, "Male", 38.65],
    ["EU Average", 2018, "Female", 33.51],
    ["EU Average", 2019, "Male", 36.36],
    ["EU Average", 2019, "Female", 34.13],
    ["EU Average", 2020, "Male", 38.39],
    ["EU Average", 2020, "Female", 33.86],
    ["EU Average", 2021, "Male", 38.75],
    ["EU Average", 2021, "Female", 34.78],
    ["EU Average", 2022, "Male", 39.34],
    ["EU Average", 2022, "Female", 35.10],
    ["EU Average", 2023, "Male", 39.67],
    ["EU Average", 2023, "Female", 35.56],
    ["EU Average", 2024, "Male", 39.93],
    ["EU Average", 2024, "Female", 35.89],
]

df = pd.DataFrame(data, columns=["Country", "Year", "Gender", "Duration"])

# Separate male and female data
male_df = df[df["Gender"] == "Male"]
female_df = df[df["Gender"] == "Female"]

plt.figure(figsize=(10, 6))

plt.plot(male_df["Year"], male_df["Duration"], marker="o", color=DARK, label="Male")
plt.plot(female_df["Year"], female_df["Duration"], marker="o", color=ORANGE, label="Female")

# Reference line at 40 years
plt.axhline(y=40, linestyle="--", linewidth=1, alpha=0.6)
plt.text(2015, 40.2, "40-year reference", fontsize=9, alpha=0.7)

plt.title("EU Average Duration of Working Life by Gender (2015–2024)")
plt.xlabel("Year")
plt.ylabel("Years in Employment")
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()