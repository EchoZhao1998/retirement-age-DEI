import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load or construct the data
# -----------------------------
data = [
    ["Albania", 65, 62, False],
    ["Argentina", 65, 60, False],
    ["Armenia", 63, 63, True],
    ["Australia", 67, 67, True],
    ["Austria", 65, 60.5, False],
    ["Azerbaijan", 65, 63.5, False],
    ["Belarus", 63, 58, False],
    ["Bangladesh", 59, 59, True],
    ["Belgium", 67, 67, True],
    ["Bosnia and Herzegovina", 65, 65, True],
    ["Brazil", 65, 62, False],
    ["Canada", 70, 70, True],
    ["China", 63, 55, False],
    ["France", 67, 67, True],
    ["Germany", 67, 67, True],
    ["Japan", 64, 62, False],
    ["South Korea", 60, 60, True],
    ["United Kingdom", 66, 66, True],
    ["United States", 70, 70, True],
    ["Vietnam", 60.5, 55.67, False]
]

df = pd.DataFrame(
    data,
    columns=["Country", "Men", "Women", "Same"]
)

# -----------------------------
# 2. Aggregate for pie chart
# -----------------------------
summary = df["Same"].value_counts().rename(
    index={True: "Same retirement age", False: "Different retirement age"}
)

# -----------------------------
# 3. Plot
# -----------------------------
fig, ax = plt.subplots(figsize=(6, 6))

colors = [ "#C97A2B", "#BDC3C7"]  # consistent, neutral palette

ax.pie(
    summary.values,
    labels=summary.index,
    autopct=lambda pct: f"{pct:.1f}%\n({int(round(pct/100*summary.sum()))})",
    startangle=90,
    colors=colors,
    textprops={"fontsize": 11}
)

ax.set_title(
    "Global Distribution of Gender-Differentiated Retirement Age Policies",
    fontsize=13,
    pad=14,
    fontweight="bold"
)

plt.tight_layout()
plt.show()