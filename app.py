import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

# Encabezado de la aplicación
st.header('Análisis de Datos de Vehículos Usados en ESTADOS UNIDOS DE AMERICA.')

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para construir un histograma
if st.button('Construir histograma'):
    st.write('Creación de un histograma para la variable "odometer" (kilometraje recorrido)')
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir un gráfico de dispersión
if st.button('Construir gráfico de dispersión'):
    st.write('Creación de un gráfico de dispersión entre el odómetro y el precio')
    fig_scatter = px.scatter(car_data, x='odometer', y='price',
                             title='Relación entre Odómetro y Precio',
                             labels={'odometer': 'Odómetro', 'price': 'Precio'})
    st.plotly_chart(fig_scatter, use_container_width=True)
