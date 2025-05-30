import folium
import pandas as pd
from . import ui as ui
from folium.plugins import MarkerCluster

out = ui.output()

df = pd.read_csv('issuerAssetHazards.csv')

m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=5)

marker_cluster = MarkerCluster().add_to(m)

for index, row in df.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']],
                  popup=f"""
                  <b>Issuer Name:</b> {row['IssuerName']}<br>
                  <b>Asset Type:</b> {row['AssetType']}<br>
                  <b>Facility Name:</b> {row['FacilityName']}<br>
                  <b>Address:</b> {row['Address']}<br>
                  <b>Latitude:</b> {row['Latitude']}<br>
                  <b>Longitude:</b> {row['Longitude']}<br>
                  """,
                  tooltip=row['IssuerName']).add_to(marker_cluster)

# m.save("rat_map.html")

with out:
    ui.show(m)
