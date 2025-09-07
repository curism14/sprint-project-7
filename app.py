import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
st.header("Análisis de Vehículos en Estados Unidos")

# ---------------------------
# Cargar los datos
# ---------------------------
# Asegúrate de que 'vehicles_us.csv' esté en la misma carpeta que app.py
car_data = pd.read_csv('vehicles_us.csv')

# ---------------------------
# Histograma
# ---------------------------
st.subheader("Histograma de Kilometraje")
st.write("Haz clic en el botón para generar un histograma de los kilometrajes (odometer) de los vehículos:")

if st.button("Mostrar Histograma"):
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        nbins=30,
        title="Distribución de Kilometraje de Vehículos",
        labels={"odometer": "Kilometraje (millas)"}
    )
    st.plotly_chart(fig_hist)

# ---------------------------
# Gráfico de dispersión
st.subheader("Gráfico de Dispersión: Precio vs Kilometraje")
st.write("Haz clic en el botón para generar un gráfico de dispersión donde se vea la relación entre precio y kilometraje:")

if st.button("Mostrar Scatter Plot"):
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Precio vs Kilometraje",
        labels={"odometer": "Kilometraje (millas)", "price": "Precio (USD)"},
        color="model_year",           # colorea por año del modelo
        # muestra modelo y condición al pasar el mouse
        hover_data=["model", "condition"]
    )
    st.plotly_chart(fig_scatter)
