import streamlit as st
import pandas as pd
import datetime

#Importamos los datos de titanic
titanic_link = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
titanic_data = pd.read_csv(titanic_link)

#Crear titulo de la webapp
st.title('Titanic App')

#Crear sidebar
sidebar=st.sidebar
sidebar.title('This is the sidebar')
sidebar.write('You can add any elements to the sidebar')

#Pedir al usuario una fecha con un calendario desplegable
today = datetime.date.today()
today_date = sidebar.date_input('Cual es tu cumpleaños',today) #puede quitarse el sidebar para centrarlo en la página
st.success(f'Tu cumpleaños es: {today_date}')

#Mostrar el contenido del dataset
st.header("Titanic Dataset")
agree = sidebar.checkbox('Show Dataset Overview')
if agree:
    st.dataframe(titanic_data)

st.markdown("___")

#Hacer una selección de Clase
st.header('Class Description')
selected_class = sidebar.radio("Select Class", titanic_data['class'].unique())
#st.write('Selected Class:', {selected_class})
st.success(f'Selected Class: {selected_class}')

st.markdown("___")

#Hacer una selección por Sexo
st.header('Sex')
selected_sex = sidebar.selectbox("Select Sex", titanic_data['sex'].unique())
st.success(f'Selected sex: {selected_sex}')
st.markdown("___")

#Hacer un slider
optionals = sidebar.expander("Optional Configurations",True)

fare_select = optionals.slider(
    "Select the Flare",
    min_value = float(titanic_data['fare'].min()),
    max_value = float(titanic_data['fare'].max())
)

subset_fare = titanic_data[(titanic_data['fare']>=fare_select)]

st.write(f"Number of Records With this Fare {fare_select}: {subset_fare.shape[0]}")
st.dataframe(subset_fare)
st.markdown("___")


