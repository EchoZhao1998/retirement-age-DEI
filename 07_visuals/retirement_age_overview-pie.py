import pandas as pd
import matplotlib.pyplot as plt
import os

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
sizes = summary.tolist()
total = sum(sizes)

# Percentages
percentages = [s / total * 100 for s in sizes]

# Colors (aligned with your site theme)
colors = ["#1F2933", "#E5E7EB"]

# Create figure
fig, ax = plt.subplots(figsize=(6, 6))

# Nudge the chart slightly to the right to make room for the legend
# Adjust position: move x0 right and reduce width to keep figure bounds
shift = 0.06
pos = ax.get_position()
new_x0 = pos.x0 + shift
new_width = max(0.1, pos.width - shift)
ax.set_position([new_x0, pos.y0, new_width, pos.height])

# Pie chart WITHOUT autopct
wedges, _ = ax.pie(
    sizes,
    colors=colors,
    startangle=90,
    wedgeprops=dict(edgecolor="white", linewidth=1)
)

ax.set_title(
    "Distribution of Statutory Retirement Age Policies by Gender",
    fontsize=24,
    pad=14
)

# Custom legend text (with % and counts)
legend_labels = [
    f"Same retirement age\n\n{percentages[0]:.1f}% ({sizes[0]} countries)",
    f"Different retirement age\n\n{percentages[1]:.1f}% ({sizes[1]} countries)"
]

ax.legend(
    wedges,
    legend_labels,
    loc="center left",
    bbox_to_anchor=(1, 0.5),
    frameon=False,
    fontsize=16,
    labelspacing=1.4,
    handletextpad=1.2
)

ax.set_aspect("equal")
plt.tight_layout()

# In headless environments `plt.show()` may not open a window.
# Save the figure next to this script so users can open it manually.
out_path = os.path.join(os.path.dirname(__file__), "retirement_age_overview-pie.png")
plt.savefig(out_path, dpi=150, bbox_inches="tight")
print(f"Saved figure to {out_path}")

plt.show()
