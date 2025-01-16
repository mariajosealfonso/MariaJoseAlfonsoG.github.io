# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/148aeJcgaxUbP5csL4O8KAMiuX76hEOu5
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Visualización de Precios de Compra/Venta y Promedio Bolsa Nacional")

# Subir archivo Excel
uploaded_file = st.file_uploader("Sube un archivo Excel", type=["xlsx"])

# Lista de hojas a procesar
sheet_names = ['EPSG - Celsia', 'ENDG', 'EPMG', 'ISGG']

if uploaded_file:
    # Mostrar las hojas disponibles y permitir seleccionar
    available_sheets = pd.ExcelFile(uploaded_file).sheet_names
    selected_sheets = st.multiselect("Selecciona las hojas a procesar", options=available_sheets, default=sheet_names)

    for sheet in selected_sheets:
        # Leer los datos de la hoja seleccionada
        data = pd.read_excel(uploaded_file, sheet_name=sheet)

        # Verificar que las columnas necesarias existan
        if all(col in data.columns for col in ['Filedate', 'Precio VENTAS', 'Precio COMPRAS', 'Prom.Bolsa.Nac']):
            file_date = data['Filedate']
            precio_ventas = data['Precio VENTAS']
            precio_compras = data['Precio COMPRAS']
            prom_bolsa_nac = data['Prom.Bolsa.Nac']

            # Crear la gráfica
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.scatter(file_date, precio_ventas, color='green', label='Precio VENTAS', alpha=0.3)
            ax.scatter(file_date, precio_compras, color='red', label='Precio COMPRAS', alpha=0.3)
            ax.plot(file_date, prom_bolsa_nac, color='black', label='Prom. Bolsa.Nac', linewidth=0.5)

            # Configurar etiquetas y título
            ax.set_xlabel('FileDate')
            ax.set_ylabel('Precios')
            ax.set_title(f'Ratio Compra/Venta vs Pbol - {sheet}')
            ax.legend()
            ax.grid()
            plt.xticks(rotation=45)

            # Mostrar la gráfica en Streamlit
            st.pyplot(fig)
        else:
            st.warning(f"La hoja '{sheet}' no contiene las columnas necesarias.")