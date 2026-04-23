import streamlit as st
import leafmap.foliumap as leafmap
from streamlit_folium import st_folium

# Set page to wide layout
st.set_page_config(layout="wide")

st.title("GeoTIFF Overlay App")

# Define columns: [1, 3] creates a 25% (left) and 75% (right) width ratio
left_col, right_col = st.columns([1, 3])

# --- Left Column: Details ---
with left_col:
    st.header("Map Details")
    st.write("This area is for your descriptions, controls, or analysis.")
    # You can add buttons, inputs, or text here
    st.info("Your GeoTIFF file is being rendered on the right.")
    st.metric(label="Layer Status", value="Active")

# --- Right Column: Map View ---
with right_col:
    tiff_path = r"C:\Users\IIT\Downloads\IIT Mandi_DTM.tif"
    
    # Initializing map near IIT Mandi
    m = leafmap.Map(center=[31.75, 77.0], zoom=13)

    try:
        m.add_raster(tiff_path, layer_name="My GeoTIFF", colormap="terrain")
        m.add_layer_control()
        
        # Display the map
        st_folium(m, use_container_width=True, height=600)
        
    except Exception as e:
        st.error(f"Error loading GeoTIFF: {e}")
        st.write("Make sure 'localtileserver' is installed via `pip install localtileserver`.")
