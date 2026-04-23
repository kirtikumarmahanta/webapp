import streamlit as st
import leafmap.foliumap as leafmap

# 1. Page Setup
st.set_page_config(layout="wide", page_title="Himachal GIS Dashboard")

st.title("Himachal Permafrost Explorer")

# 2. Define Layout
col1, col2 = st.columns([1, 3])

# 3. Sidebar/Control Panel
with col1:
    st.header("Layer Controls")
    st.markdown("Adjust visualization parameters below.")
    
    # Slider for interactivity
    opacity = st.slider("Raster Opacity", 0.0, 1.0, 0.7)
    
    st.divider()
    st.subheader("Map Information")
    st.info("""
    **Layer Details:**
    - File: Permafrost_Himachal.tif
    - Region: Himachal Pradesh
    - Source: Cloudflare R2
    """)

# 4. Map Container
with col2:
    # Your R2 Public URL
    raster_url = "https://pub-927b7ce233e44225b6e9fdd2839b44cf.r2.dev/Permafrost_Himachal.tif"
    
    # Initialize Map (Centered on Himachal Pradesh)
    m = leafmap.Map(center=[31.6, 77.3], zoom=8)
    m.add_basemap("OpenStreetMap")
    
    try:
        # Add Raster
        m.add_raster(
            raster_url, 
            layer_name="Permafrost Layer", 
            colormap="terrain", 
            opacity=opacity
        )
        
        # Add Legend
        m.add_legend(title="Elevation Data", builtin_legend="terrain")
        
        # Render
        m.to_streamlit(height=600)
        
    except Exception as e:
        st.error("Could not load the raster layer.")
        st.write("Troubleshooting Checklist:")
        st.write("1. Check your browser console (F12) for CORS errors.")
        st.write("2. Ensure the bucket CORS policy is set to '*' .")
        st.write("3. Ensure your file is a Cloud Optimized GeoTIFF (COG).")
        st.exception(e)
