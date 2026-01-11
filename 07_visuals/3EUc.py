import pandas as pd
import matplotlib.pyplot as plt

data = [
    ["Germany", 2015, "Male", 40.0], ["Germany", 2016, "Male", 40.2],
    ["Germany", 2017, "Male", 40.4], ["Germany", 2018, "Male", 40.7],
    ["Germany", 2019, "Male", 39.1], ["Germany", 2020, "Male", 40.6],
    ["Germany", 2021, "Male", 40.5], ["Germany", 2022, "Male", 41.2],
    ["Germany", 2023, "Male", 41.4], ["Germany", 2024, "Male", 41.7],
    ["Germany", 2015, "Female", 35.7], ["Germany", 2016, "Female", 36.0],
    ["Germany", 2017, "Female", 36.3], ["Germany", 2018, "Female", 36.5],
    ["Germany", 2019, "Female", 36.9], ["Germany", 2020, "Female", 36.7],
    ["Germany", 2021, "Female", 36.7], ["Germany", 2022, "Female", 37.3],
    ["Germany", 2023, "Female", 37.7], ["Germany", 2024, "Female", 38.1],

    ["Italy", 2015, "Male", 35.4], ["Italy", 2016, "Male", 35.9],
    ["Italy", 2017, "Male", 36.2], ["Italy", 2018, "Male", 36.4],
    ["Italy", 2019, "Male", 36.4], ["Italy", 2020, "Male", 35.7],
    ["Italy", 2021, "Male", 35.9], ["Italy", 2022, "Male", 36.5],
    ["Italy", 2023, "Male", 37.2], ["Italy", 2024, "Male", 37.2],
    ["Italy", 2015, "Female", 25.7], ["Italy", 2016, "Female", 26.3],
    ["Italy", 2017, "Female", 26.8], ["Italy", 2018, "Female", 27.1],
    ["Italy", 2019, "Female", 27.3], ["Italy", 2020, "Female", 26.4],
    ["Italy", 2021, "Female", 26.9], ["Italy", 2022, "Female", 27.6],
    ["Italy", 2023, "Female", 28.3], ["Italy", 2024, "Female", 28.2],

    ["Sweden", 2015, "Male", 42.2], ["Sweden", 2016, "Male", 42.2],
    ["Sweden", 2017, "Male", 42.6], ["Sweden", 2018, "Male", 42.7],
    ["Sweden", 2019, "Male", 43.0], ["Sweden", 2020, "Male", 43.2],
    ["Sweden", 2021, "Male", 43.5], ["Sweden", 2022, "Male", 43.7],
    ["Sweden", 2023, "Male", 44.1], ["Sweden", 2024, "Male", 44.0],
    ["Sweden", 2015, "Female", 40.1], ["Sweden", 2016, "Female", 40.3],
    ["Sweden", 2017, "Female", 40.7], ["Sweden", 2018, "Female", 40.9],
    ["Sweden", 2019, "Female", 41.1], ["Sweden", 2020, "Female", 40.6],
    ["Sweden", 2021, "Female", 40.8], ["Sweden", 2022, "Female", 41.3],
    ["Sweden", 2023, "Female", 41.9], ["Sweden", 2024, "Female", 42.0],
]

df = pd.DataFrame(data, columns=["Country", "Year", "Gender", "Duration"])

countries = ["Germany", "Italy", "Sweden"]

plt.figure(figsize=(12, 8))

for i, country in enumerate(countries, 1):
    plt.subplot(2, 2, i)
    subset = df[df["Country"] == country]

    for gender in ["Male", "Female"]:
        gdata = subset[subset["Gender"] == gender]
        plt.plot(gdata["Year"], gdata["Duration"], marker="o", label=gender)

    plt.axhline(40, linestyle="--", linewidth=1, alpha=0.5)
    plt.title(country)
    plt.xlabel("Year")
    plt.ylabel("Working-life duration")
    plt.grid(alpha=0.3)
    plt.legend()

plt.tight_layout()
plt.show()