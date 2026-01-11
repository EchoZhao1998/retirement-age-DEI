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
        colors.append("#2C3E50")   # differentiated regimes

# -----------------------------
# 4. Plot
# -----------------------------
fig, ax = plt.subplots(figsize=(8, 12))

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

# -----------------------------
# 5. Annotate China
# -----------------------------
china_row = df[df["Country"] == "China"]
ax.text(
    china_row["Gap"].values[0] + 0.1,
    china_row.index[0],
    "China (8 years)",
    va="center",
    fontsize=10,
    color="#E74C3C"
)

plt.tight_layout()
plt.show()