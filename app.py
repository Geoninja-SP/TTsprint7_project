import pandas as pd
import plotly.express as px
import streamlit as st


# Encabezado
st.header("📊 Análisis de anuncios de vehículos")

car_data = pd.read_csv(
    "C:/Users/spaub/Documents/Tripleten/Sprint7/Proyecto/vehicles_us.csv")
# crear un botón para el histograma
hist_button = st.button('Construir histograma')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

    # Botón para gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión entre precio y kilometraje')
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Relación entre kilometraje y precio",
        labels={"odometer": "Kilometraje", "price": "Precio (USD)"},
        opacity=0.6
    )
    st.plotly_chart(fig, use_container_width=True)

# Botón 3: Barras (precio promedio por tipo)
bar_button = st.button('Construir gráfico de barras')

if bar_button:
    st.write('Creación de un gráfico de barras: precio promedio por tipo de vehículo (filtrando outliers)')

    # Filtrar outliers
    filtered = car_data[car_data["price"] < 100000]

    # Agrupar por tipo y calcular promedio
    avg_price_by_type = filtered.groupby(
        "type", as_index=False)["price"].mean()

    # Gráfico de barras
    fig = px.bar(
        avg_price_by_type,
        x="type",
        y="price",
        title="Precio promedio por tipo de vehículo (filtrado < 100k USD)",
        labels={"type": "Tipo de vehículo", "price": "Precio promedio (USD)"},
        color="type",
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    st.plotly_chart(fig, use_container_width=True)
