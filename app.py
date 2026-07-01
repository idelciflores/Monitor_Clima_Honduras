import streamlit as st
import pandas as pd
from api_client import consultar_api

st.set_page_config(page_title="Mi Clima Cloud")

st.title("Mi Monitor de Clima")
st.write("---")

st.write("### ¿Dónde quieres revisar el clima?")
mi_ciudad = st.selectbox(
    "Elige una ciudad de Honduras:",
    ["Tegucigalpa", "San Pedro Sula", "Choluteca", "Santa Rosa de Copán"]
)

mapa_ciudades = {
    "Tegucigalpa": {"lat": 14.10, "lon": -87.21},
    "San Pedro Sula": {"lat": 15.50, "lon": -88.03},
    "Choluteca": {"lat": 13.33, "lon": -87.19},
    "Santa Rosa de Copán": {"lat": 14.76, "lon": -88.77}
}

if st.button("Ver reporte actual"):
    lat = mapa_ciudades[mi_ciudad]["lat"]
    lon = mapa_ciudades[mi_ciudad]["lon"]
    
    info_clima = consultar_api(lat, lon)
    
    if info_clima:
        temp_actual = info_clima["current"]["temperature_2m"]
        humedad = info_clima["current"]["relative_humidity_2m"]
        
        st.write(f"## Actualmente en {mi_ciudad}: **{temp_actual}°C**")
        
        col1, col2 = st.columns(2)
        col1.metric("Humedad", f"{humedad}%")
        
        if temp_actual > 28:
            col2.warning("¡Mucho calor! Hidrátate bien.")
        elif temp_actual < 18:
            col2.info("Está fresquito, usa un suéter.")
        else:
            col2.success("Clima agradable.")

        st.write("### Variación de temperatura para hoy")
        datos_grafico = pd.DataFrame({
            "Grados": info_clima["hourly"]["temperature_2m"][:24]
        })
        st.area_chart(datos_grafico, color="#29b5e8")
        
        with st.expander("Ver datos técnicos"):
            st.table(datos_grafico.head(5))
            
    else:
        st.error("Lo siento, no pude conectar con el satélite.")

st.write("---")
st.caption("Proyecto de Computación en la Nube @2026 - Idelci Flores")