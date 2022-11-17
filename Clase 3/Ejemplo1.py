import streamlit as st
import pandas as pd
import numpy as np

st.title("Aplicando la SideBar")
sidebar = st.sidebar
sidebar.title("titulo de mi barra")

sidebar.write("Info en el sidebar")

st.header("Header de la app")
st.write("info de la app")

if sidebar.checkbox("Show datafreame"):
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=['a','b','c'])

    st.dataframe(chart_data)