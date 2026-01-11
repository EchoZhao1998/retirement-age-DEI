import pandas as pd
import matplotlib.pyplot as plt

ORANGE = "#C97A2B"
DARK = "#1F2933"

# Create dataframe
data = {
    "Year": [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015],
    "Total": [73439, 74041, 73351, 74652, 75064, 75447, 75782, 76058, 76245, 76320],
    "Urban": [47345, 47032, 45931, 46773, 46271, 45249, 44292, 43208, 42051, 40916],
    "Rural": [26094, 27009, 27420, 27879, 28793, 30198, 31490, 32850, 34194, 35404]
}

df = pd.DataFrame(data)
df = df.sort_values("Year")  # ensure chronological order

plt.figure(figsize=(10, 6))

plt.plot(df["Year"], df["Urban"], marker="o", color=ORANGE, label="Urban employment")
plt.plot(df["Year"], df["Rural"], marker="o", color=DARK, label="Rural employment")
plt.plot(df["Year"], df["Total"], linestyle="--", alpha=0.6, label="Total employment")

plt.title("China Employment Structure Change (2015–2024)")
plt.xlabel("Year")
plt.ylabel("Employed persons (10,000)")
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()

# Add female participation data
df["Female_LFPR"] = [
    59.562, 59.948, 59.894, 61.181, 59.908,
    61.248, 61.533, 61.911, 62.286, 62.571
]

plt.figure(figsize=(10, 6))

ax1 = plt.gca()
ax2 = ax1.twinx()

# Left axis: total employment
ax1.plot(df["Year"], df["Total"], marker="o", color=DARK, label="Total employment")
ax1.set_xlabel("Year")
ax1.set_ylabel("Employed persons (10,000)", color=DARK)

# Right axis: female participation rate
ax2.plot(df["Year"], df["Female_LFPR"], linestyle="--", marker="s", color=ORANGE, label="Female LFPR (%)")
ax2.set_ylabel("Female labor force participation rate (%)", color=ORANGE)

# Titles and grid
plt.title("China: Employment Decline vs Female Participation Trend")
ax1.grid(alpha=0.3)

# Combine legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper center")

plt.tight_layout()
plt.show()