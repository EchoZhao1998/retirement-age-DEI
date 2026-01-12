import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ORANGE = "#C97A2B"
DARK = "#1F2933"
# -----------------------------
# Data
# -----------------------------
data = {
    "Country": [
        "United States", "Canada", "United Kingdom", "Australia", 
        "Finland", "Germany", "Italy",
        "Japan", "South Korea", "Hong Kong",
        "China", "Thailand", "Brazil"
    ],
    "Men": [70, 66, 67, 70, 69, 67, 67, 65, 64, 60, 63, 60, 65],
    "Women": [70, 66, 67, 70, 69, 67, 67, 65, 62, 60, 58, 60, 62]
}

df = pd.DataFrame(data)

# -----------------------------
# X positions
# -----------------------------
countries = df["Country"]
x = np.arange(len(countries))

# Gap between Men and Women groups
gap = 1.5
x_men = x
x_women = x + len(x) + gap

# -----------------------------
# Plot
# -----------------------------
plt.figure(figsize=(18, 6))

bar_width = 0.5

colors = {
    "Men": DARK,      
    "Women": ORANGE    
}

plt.bar(x_men, df["Men"], width=bar_width, color=colors["Men"])
plt.bar(x_women, df["Women"], width=bar_width, color=colors["Women"])

# -----------------------------
# Axes & labels
# -----------------------------
all_x = np.concatenate([x_men, x_women])
all_labels = list(countries) + list(countries)

plt.xticks(all_x, all_labels, rotation=45, ha="right")
plt.ylabel("Statutory Retirement Age")
plt.ylim(50, 75)
plt.grid(alpha=0.3, axis="y")

# Reference line at 70 years
# plt.axhline(y=70, linestyle="--", linewidth=1, alpha=0.6)

# -----------------------------
# Section titles
# -----------------------------
plt.text(
    x_men.mean(), 73, "MEN",
    ha="center", va="bottom", fontsize=12, fontweight="bold"
)

plt.text(
    x_women.mean(), 73, "WOMEN",
    ha="center", va="bottom", fontsize=12, fontweight="bold"
)

# -----------------------------
# Legend
# -----------------------------
legend_handles = [
    plt.Rectangle((0, 0), 1, 1, color=colors["Men"]),
    plt.Rectangle((0, 0), 1, 1, color=colors["Women"])
]
plt.legend(legend_handles, ["Men", "Women"], frameon=False)

plt.title("Statutory Retirement Age by Gender and Country")
plt.tight_layout()
plt.show()