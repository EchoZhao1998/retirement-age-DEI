import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# -----------------------------
# 1. Data
# -----------------------------
data = {
    "country": [
        "Belgium","Bulgaria","Czechia","Denmark","Germany","Estonia","Ireland",
        "Greece","Spain","France","Croatia","Italy","Cyprus","Latvia","Lithuania",
        "Luxembourg","Hungary","Malta","Netherlands","Austria","Poland","Portugal",
        "Romania","Slovenia","Slovakia","Finland","Sweden","Iceland","Norway",
        "Switzerland","Serbia","Türkiye"
    ],
    "duration": [
        35.0,34.8,37.5,42.5,40.0,41.4,40.4,
        34.8,36.5,37.2,34.8,32.8,39.0,37.4,38.5,
        35.6,37.4,39.0,43.8,38.7,35.5,39.3,
        32.7,37.1,36.0,39.8,43.0,46.3,41.2,
        42.8,35.5,30.2
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# 2. World map
# -----------------------------
world = gpd.read_file(
    "data/maps/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp"
)

# Fix naming mismatches
world["name"] = world["name"].replace({
    "Czech Rep.": "Czechia",
    "Turkey": "Türkiye"
})

gdf = world.merge(df, left_on="name", right_on="country", how="left")

# -----------------------------
# 3. Theme color map (orange scale)
# -----------------------------
theme_cmap = LinearSegmentedColormap.from_list(
    "theme_orange",
    ["#F6EFE6", "#E4B27A", "#C97A2B"]
)

# -----------------------------
# 4. Plot
# -----------------------------
fig, ax = plt.subplots(1, 1, figsize=(12, 10))

gdf.plot(
    column="duration",
    cmap=theme_cmap,
    linewidth=0.6,
    edgecolor="#1F2933",
    ax=ax,
    missing_kwds={
        "color": "#E5E7EB",
        "label": "No data"
    }
)

ax.set_title(
    "Expected Duration of Working Life in Europe (2024)",
    fontsize=14,
    color="#1F2933",
    pad=16
)

ax.axis("off")

# Colorbar
sm = plt.cm.ScalarMappable(
    cmap=theme_cmap,
    norm=plt.Normalize(
        vmin=df["duration"].min(),
        vmax=df["duration"].max()
    )
)
sm._A = []

cbar = fig.colorbar(sm, ax=ax, fraction=0.03, pad=0.02)
cbar.set_label("Years", color="#1F2933")
cbar.ax.tick_params(colors="#1F2933")

plt.tight_layout()
plt.show()