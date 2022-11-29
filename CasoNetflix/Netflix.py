import streamlit as st
import pandas as pd

st.title('Streamlit - Netflix')
sidebar = st.sidebar

DATA_URL = 'movies.csv'

#CARGAR DATOS POR NOMBRE DE PELÍCULA.
#Toma como argumento el nombre de la película ingresado por el usuario
@st.cache
def load_data_byname(name):
    data = pd.read_csv(DATA_URL)
    filtered_data_byname = data[data['name'].str.upper().str.contains(name)]
    return filtered_data_byname

#FILTRAR DATOS POR NOMBRE DE PELÍCULA-------------
myname = sidebar.text_input('Nombre de la pelicula: ')
btnname = sidebar.button('Buscar por nombre')
if (btnname):
    filterbyname = load_data_byname(myname.upper())
    count_row = filterbyname.shape[0]
    st.write(f"Peliculas Totales: {count_row}")
    st.dataframe(filterbyname)
    
#Cargar datos por director de película
@st.cache
def load_data_bydirector(director):
    data = pd.read_csv(DATA_URL)
    filtered_data_bydirector = data[data['director'].str.contains(director)]
    return filtered_data_bydirector

#Cargar datos en general
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

data = load_data()

#FILTRAR DATOS POR DIRECTOR-----------
director = sidebar.selectbox('Nombre del Director: ',data['director'].unique()) #Se selecciona el director
btndirector = st.sidebar.button('Buscar por Director')                          #Se ejecuta la busqueda

#Lógica de botón
if (btndirector):                                       #Si se cambia el estado del botón
    filterbydirector = load_data_bydirector(director)   #se cargan los datos
    count_row = filterbydirector.shape[0]               #se cuentan las películas del director seleccionado
    st.write(f"Peliculas Totales: {count_row}")         #Mmostrar la cantidad de películas del director seleccionado
    st.dataframe(filterbydirector)                      #mostrar las películas del director seleccionado