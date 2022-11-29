import streamlit as st
import pandas as pd

DATA_URL = 'uber-raw-data-sep14.csv'

st.title("Viajes UBER")
st.write("El propósito de este dashboard es determinar tendencias en los viajes de uber en relación con la hora y puntos de inicio de viaje en una ciudad")

st.header("Viajes de Uber en la ciudad de Nueva Yorkcon filtros por hora.")

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data['date/time'] = pd.to_datetime(data['date/time'])
    data['time_hour'] = pd.to_datetime(data['date/time']).dt.hour
   
    return data

data = load_data(1000)

hour_select = st.slider(
    "Selecciona la Hora",
    min_value = int(data['time_hour'].min()),
    max_value = int(data['time_hour'].max()),
    step=1
)

subset_hour = data[(data['time_hour']==hour_select)]

st.dataframe(subset_hour)
st.map(subset_hour[['lat','lon']])
