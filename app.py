import streamlit as st
import leafmap.foliumap as leafmap

# 1. Set the page to wide mode to maximize map area
st.set_page_config(layout="wide", page_title="GIS Dashboard")

st.title("GIS Data Explorer")

# 2. Define the columns
# The list [1, 3] creates a ratio: 1/4 of width for info, 3/4 for map
col1, col2 = st.columns([1, 3])

with col1:
    st.header("Layer Controls")
    st.markdown("Use this panel to adjust your data visualization parameters.")
    
    # Example interactive control
    opacity = st.slider("Raster Opacity", 0.0, 1.0, 0.7)
    
    st.info("Metadata:\n- File: satellite_v1.tif\n- CRS: EPSG:4326\n- Source: Cloudflare R2")

with col2:
    # 3. Render the Map
    # Ensure this URL is your public Cloudflare R2 direct link
    raster_url = "https://pub-927b7ce233e44225b6e9fdd2839b44cf.r2.dev/Permafrost_Himachal.tif"
    
    m = leafmap.Map(center=[20, 0], zoom=3)
    m.add_basemap("OpenStreetMap")
    
    try:
        m.add_raster(
            raster_url, 
            layer_name="Satellite Layer", 
            colormap="terrain", 
            opacity=opacity  # Uses the variable from the slider in col1
        )
        m.to_streamlit(height=600)
    except Exception as e:
        st.error(f"Map failed to load: {e}")
