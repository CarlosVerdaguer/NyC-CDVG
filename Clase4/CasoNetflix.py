import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#--- IMPORT DATA ---#
@st.cache
def load_data(nrows=500):
    df = pd.read_csv('movies.csv', nrows=10)
    return df


#--- PAGE CONFIG ---#
st.set_page_config(page_title="Caso Netflix")

st.dataframe(load_data(500))