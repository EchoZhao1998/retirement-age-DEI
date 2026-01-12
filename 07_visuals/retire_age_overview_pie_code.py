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
summary = df["Same"].value_counts()
same_count = summary[True]
diff_count = summary[False]
total = same_count + diff_count

# Percentages
same_pct = same_count / total * 100
diff_pct = diff_count / total * 100

# -----------------------------
# 3. Plot (clean version)
# -----------------------------
fig, ax = plt.subplots(figsize=(8, 8))

colors = ["#1F2933", "#E5E7EB"]  # dark primary + neutral contrast

wedges, _ = ax.pie(
    [same_count, diff_count],
    colors=colors,
    startangle=90,
    wedgeprops=dict(edgecolor="white", linewidth=1)
)

ax.set_title(
    "Global Distribution of Gender-Differentiated Retirement Age Policies",
    fontsize=24,
    pad=14,
    fontweight="bold"
)

# Custom legend with figures UNDER labels
legend_labels = [
    f"Same retirement age\n{same_pct:.1f}% ({same_count} countries)",
    f"Different retirement age\n{diff_pct:.1f}% ({diff_count} countries)"
]

ax.legend(
    wedges,
    legend_labels,
    loc="center left",
    bbox_to_anchor=(2.0, 1.0),
    frameon=False,
    fontsize=14
)

ax.set_aspect("equal")
plt.tight_layout()
plt.show()