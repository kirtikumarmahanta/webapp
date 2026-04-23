import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.title("Debug Map")

# URL of your file
raster_url = "https://pub-927b7ce233e44225b6e9fdd2839b44cf.r2.dev/Permafrost_Himachal.tif"

m = leafmap.Map(center=[31.6, 77.3], zoom=8)
m.add_basemap("OpenStreetMap")

# Add raster WITHOUT the legend
# We force the CRS to EPSG:4326 to ensure leafmap knows where to place it
m.add_raster(raster_url, layer_name="Test Layer", colormap="terrain", crs="EPSG:4326")

m.to_streamlit(height=600)
