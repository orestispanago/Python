import geopandas as gpd
import pandas as pd

DIAMETER_KM = 120

data = {
    "Name": ["Taif", "Baha", "Abha", "Riyadh", "Qassim", "Hail"],
    "Longitude": [40.5606, 41.6426, 42.6529, 46.7219, 43.7638, 41.6898],
    "Latitude": [21.4799, 20.2951, 18.2373, 24.9252, 26.3118, 27.435],
}
df = pd.DataFrame(data)

gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df["Longitude"], df["Latitude"]),
    crs="EPSG:4326",
)

gdf_metric = gdf.to_crs(epsg=32638)
gdf_metric["geometry"] = gdf_metric.geometry.buffer(int(DIAMETER_KM * 1000))
gdf_final = gdf_metric.to_crs(epsg=4326)
output_filename = f"buffers_{DIAMETER_KM}km.shp"
gdf_final.to_file(output_filename)
