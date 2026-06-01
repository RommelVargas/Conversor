from engine import convertir_temperatura, convertir_presion
import streamlit as st

m = "Hola"

# --- INTERFAZ DE USUARIO ---

st.title("Convertidor de Unidades")

# Menú lateral
modo = st.sidebar.selectbox("Selecciona qué deseas convertir:", ["Temperatura", "Presión"])

# Layout en columnas para hacerlo más estético
col1, col2, col3 = st.columns([2, 1, 2])

if modo == "Temperatura":
    unidades_temp = ['Celsius', 'Fahrenheit', 'Kelvin', 'Rankine']
    
    with col1:
        unidad_origen = st.selectbox("De:", unidades_temp)
        valor_origen = st.number_input("Valor:", value=0.0, format="%.2f")
        
    with col3:
        unidad_destino = st.selectbox("A:", unidades_temp)
        
    # Cálculo
    resultado = convertir_temperatura(valor_origen, unidad_origen, unidad_destino)
    
    with col3:
        st.write("### Resultado:")
        st.success(f"{resultado:.2f} {unidad_destino}")

elif modo == "Presión":
    unidades_pres = ['Pascal', 'Atmósfera', 'Bar', 'PSI', 'Milímetros de mercurio']
    
    with col1:
        unidad_origen = st.selectbox("De:", unidades_pres)
        valor_origen = st.number_input("Valor:", value=1.0, format="%.4f")
        
    with col3:
        unidad_destino = st.selectbox("A:", unidades_pres)
        
    # Cálculo
    resultado = convertir_presion(valor_origen, unidad_origen, unidad_destino)
    
    with col3:
        st.write("### Resultado:")
        st.success(f"{resultado:.4f} {unidad_destino}")