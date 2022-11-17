import streamlit as st
import pandas as pd
import numpy as np

map_data = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
columns=['latitude', 'longitude'])

# Create the title for the web app
st.title("San francisco Map")
st.header("Using Streamlit and Mapbox")

#Creamos el mapa
st.map(map_data)