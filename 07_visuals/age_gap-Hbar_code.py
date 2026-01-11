import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Construct the dataset
# -----------------------------
data = [
    ["Albania", 3],
    ["Argentina", 5],
    ["Armenia", 0],
    ["Australia", 0],
    ["Austria", 4.5],
    ["Azerbaijan", 1.5],
    ["Belarus", 5],
    ["Bangladesh", 0],
    ["Belgium", 0],
    ["Brazil", 3],
    ["Canada", 0],
    ["Chile", 5],
    ["China", 8],
    ["Colombia", 5],
    ["Croatia", 1],
    ["Cuba", 5],
    ["France", 0],
    ["Germany", 0],
    ["India", 0],
    ["Iran", 5],
    ["Italy", 0],
    ["Japan", 2],
    ["Kazakhstan", 5],
    ["Lithuania", 1],
    ["Moldova", 2],
    ["Montenegro", 2],
    ["North Korea", 5],
    ["Oman", 5],
    ["Poland", 5],
    ["Romania", 3],
    ["Russia", 5],
    ["Serbia", 1.5],
    ["Turkey", 2],
    ["Uzbekistan", 5],
    ["Venezuela", 5],
    ["Vietnam", 4.83]
]

df = pd.DataFrame(data, columns=["Country", "Gap"])

# -----------------------------
# 2. Sort by gap
# -----------------------------
df = df.sort_values("Gap", ascending=True)

# -----------------------------
# 3. Define colors
# -----------------------------
colors = []
for country, gap in zip(df["Country"], df["Gap"]):
    if country == "China":
        colors.append("#C97A2B")   # highlight China
    elif gap == 0:
        colors.append("#D0D3D4")   # same-age regimes
    else:
        colors.append("#1F2933")   # differentiated regimes

# -----------------------------
# 4. Plot
# -----------------------------
ffig, ax = plt.subplots(figsize=(8, 12))

ax.barh(
    df["Country"],
    df["Gap"],
    color=colors
)

ax.set_xlabel("Retirement Age Gap (Men − Women, Years)", fontsize=11)
ax.set_title(
    "Statutory Gender Gap in Retirement Age by Country",
    fontsize=13,
    pad=12
)

# X-axis grid for year scale
ax.xaxis.grid(
    True,
    linestyle="--",
    linewidth=0.8,
    alpha=0.4
)
ax.set_axisbelow(True)

# Annotate China (raised position)
china_row = df[df["Country"] == "China"]
china_y = china_row.index[0]

ax.text(
    china_row["Gap"].values[0] + 0.1,
    china_y - 0.1,
    "China (8 years)",
    fontsize=10,
    color="#C97A2B",
    ha="left",
    va="center"
)

plt.tight_layout()
plt.show()