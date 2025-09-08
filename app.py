import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header("Visualización de datos de vehículos")

# Casillas de verificación
show_histogram = st.checkbox("Mostrar histograma de odómetro")
show_scatter = st.checkbox("Mostrar gráfico de dispersión precio vs odómetro")

# Mostrar histograma si se selecciona la casilla
if show_histogram:
    fig_hist = px.histogram(car_data, x="odometer",
                            nbins=50, title="Histograma de Odometer")
    st.write("Histograma de Odometer")
    st.plotly_chart(fig_hist)

# Mostrar gráfico de dispersión si se selecciona la casilla
if show_scatter:
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        # columnas disponibles
        hover_data=["model", "model_year", "condition"],
        color="fuel",  # opcional: colorear por tipo de combustible
        title="Precio vs Odometer"
    )
    st.write("Gráfico de dispersión Precio vs Odometer")
    st.plotly_chart(fig_scatter)
