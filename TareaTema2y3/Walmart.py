import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff

#IMPORTAR DATOS
DATA_URL = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'

@st.cache
def first_load(data):
    data = pd.read_csv(data)
    return data
data = first_load(DATA_URL)

#LAYOUT DE LA PÁGINA
st.title("Walmart USA")
st.header("Datos de ventas de Walmart en Estados Unidos")

st.write("Este dashboard tiene el propósito de analizar los datos de ventas de walmart en estados unidos. Esto con el propósito de entender")
st.write("más a fondo las tendencias de compra y de logística del retailer comercial")

sidebar = st.sidebar

#FILTRAR DATOS POR CATEGORÍA
Category = data['Category'].unique().tolist()
categ = sidebar.selectbox('¿Que Categoria quieres ver?', Category,0)
data = data[data['Category']==categ]

#FILTRAR DATOS POR CLASE
selected_class = sidebar.radio("Selecciona una clase",data['Ship Mode'].unique())
sidebar.write("Selected Class:", selected_class)
data = data[data['Ship Mode']==selected_class]

#EXPANDER PARA SELECCIONAR DESCUENTO
optionals = st.expander("Descuento", True)

#HACER SLIDER DEL FARE
fare_select = optionals.slider(
"Select the Fare",
min_value=float(data['Discount'].min()),
max_value=float(data['Discount'].max())
)

data = data[(data['Discount'] >= fare_select)]


#CHECKBOX
agree = sidebar.checkbox("show DataSet Overview ? ")
if agree:

    st.dataframe(data)

data = pd.read_csv(DATA_URL)
fig2, ax2 = plt.subplots()
y_pos = data['Ship Mode']
x_pos = data['Sales']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Clase")
ax2.set_xlabel("Ventas")
ax2.set_title('Ventas por clase')
st.header("Grafica de Barras de Walmart")
st.pyplot(fig2)

data = pd.read_csv(DATA_URL)
df_p = data.groupby(['Region']).size().reset_index()
df_p.columns = ['Region' ,'Counts']
df_p['percentage'] = df_p.groupby(['Counts']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
df_p.columns = ['Region' ,'Counts', 'Percentage']
df_p['Percentage'] = (df_p['Counts'] / df_p['Counts'].sum()) * 100

fig1, ax1 = plt.subplots()
ax1.pie(df_p['Percentage'], labels=df_p['Region'], autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  
st.header("Ventas por región de WaltMart USA")

st.pyplot(fig1)

st.header("Histograma de descuentos WaltMart USA")
fig, ax = plt.subplots()
ax.hist(data['Discount'], bins=20)

st.pyplot(fig)

@st.cache
def load_data(nrows):
    DATA_URL = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data['Order Date'] = pd.to_datetime(data['Order Date'])
    return data

data = load_data(100)

st.dataframe(data)