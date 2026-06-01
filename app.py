from engine import convertir_temperatura, convertir_unidades, SISTEMAS_LINEALES
import streamlit as st

# --- INTERFAZ DE USUARIO ---

st.title("Convertidor de Unidades")

# El menú se alimenta automáticamente de las llaves de tu diccionario maestro
opciones_menu = ["Temperatura"] + list(SISTEMAS_LINEALES.keys())
modo = st.sidebar.selectbox("Selecciona qué deseas convertir:", opciones_menu)

col1, col2, col3 = st.columns([2, 1, 2])

if modo == "Temperatura":
    unidades_temp = ['Celsius', 'Fahrenheit', 'Kelvin', 'Rankine']
    
    with col1:
        unidad_origen = st.selectbox("De:", unidades_temp)
        valor_origen = st.number_input("Valor:", value=0.0, format="%.2f")
        
    with col3:
        unidad_destino = st.selectbox("A:", unidades_temp)
        
    resultado = convertir_temperatura(valor_origen, unidad_origen, unidad_destino)
    
    with col3:
        st.write("### Resultado:")
        st.success(f"{resultado:.2f} {unidad_destino}")

else:
    # Extraemos el diccionario específico que el usuario eligió
    diccionario_actual = SISTEMAS_LINEALES[modo]
    
    # Extraemos las unidades de ese diccionario
    unidades_disponibles = list(diccionario_actual.keys())
    
    with col1:
        unidad_origen = st.selectbox("De:", unidades_disponibles)
        valor_origen = st.number_input("Valor:", value=1.0, format="%.4f")
        
    with col3:
        unidad_destino = st.selectbox("A:", unidades_disponibles)
        
    # Magia: Llamamos a la función universal pasándole el diccionario_actual
    resultado = convertir_unidades(valor_origen, unidad_origen, unidad_destino, diccionario_actual)
    
    with col3:
        st.write("### Resultado:")
        st.success(f"{resultado:.4f} {unidad_destino}")