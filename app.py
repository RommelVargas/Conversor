import streamlit as st

# --- FUNCIONES DE CONVERSIÓN ---

def convertir_temperatura(valor, de_unidad, a_unidad):
    # Primero pasamos todo a Kelvin como unidad base para no hacer tantas combinaciones
    if de_unidad == 'Celsius':
        k = valor + 273.15
    elif de_unidad == 'Fahrenheit':
        k = (valor - 32) * 5/9 + 273.15
    elif de_unidad == 'Rankine':
        k = valor * 5/9
    else: # Ya es Kelvin
        k = valor
        
    # Ahora pasamos de Kelvin a la unidad deseada
    if a_unidad == 'Celsius':
        return k - 273.15
    elif a_unidad == 'Fahrenheit':
        return (k - 273.15) * 9/5 + 32
    elif a_unidad == 'Rankine':
        return k * 9/5
    else:
        return k

def convertir_presion(valor, de_unidad, a_unidad):
    # Factores de conversión tomando el Pascal (Pa) como base
    factores_pa = {
        'Pascal (Pa)': 1,
        'Atmósfera (atm)': 101325,
        'Bar': 100000,
        'PSI': 6894.76,
        'Milímetros de mercurio (mmHg)': 133.322
    }
    
    # Lógica: Convertir a Pa y luego dividir por el factor de la unidad destino
    valor_en_pa = valor * factores_pa[de_unidad]
    resultado = valor_en_pa / factores_pa[a_unidad]
    return resultado

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