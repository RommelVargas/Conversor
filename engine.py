
DICCIONARIO_MASA = {
    'Kilogramo (kg)': 1.0,
    'Gramo (g)': 0.001,
    'Miligramo (mg)': 0.000001,
    'Libra (lb)': 0.45359237,      
    'Onza (oz)': 0.0283495237,    
    'Tonelada (t)': 1000.0
}
DICCIONARIO_PRESION = {
    'Pascal': 1,
    'Atmósfera': 101325,
    'Bar': 100000,
    'PSI': 6894.76,
    'Milímetros de mercurio': 133.322
}
# --- LONGITUD (Base: Metro) ---
DICCIONARIO_LONGITUD = {
    'Metro (m)': 1.0,
    'Centímetro (cm)': 0.01,
    'Milímetro (mm)': 0.001,
    'Kilómetro (km)': 1000.0,
    'Pulgada (in)': 0.0254,
    'Pie (ft)': 0.3048,
    'Yarda (yd)': 0.9144,
    'Milla (mi)': 1609.34
}

DICCIONARIO_VOLUMEN = {
    'Litro (L)': 1.0,
    'Mililitro (mL)': 0.001,
    'Metro cúbico (m³)': 1000.0,
    'Galón (US gal)': 3.78541,
    'Onza líquida (US fl oz)': 0.0295735,
    'Barril de petróleo (bbl)': 158.987 
}

DICCIONARIO_ENERGIA = {
    'Joule (J)': 1.0,
    'Kilojoule (kJ)': 1000.0,
    'Caloría (cal)': 4.184,
    'Kilocaloría (kcal)': 4184.0,
    'BTU': 1055.06,
    'Kilovatio-hora (kWh)': 3600000.0
}

def convertir_temperatura(valor, de_unidad, a_unidad):
    if de_unidad == 'Celsius':
        k = valor + 273.15
    elif de_unidad == 'Fahrenheit':
        k = (valor - 32) * 5/9 + 273.15
    elif de_unidad == 'Rankine':
        k = valor * 5/9
    else: 
        k = valor
        
    if a_unidad == 'Celsius':
        return k - 273.15
    elif a_unidad == 'Fahrenheit':
        return (k - 273.15) * 9/5 + 32
    elif a_unidad == 'Rankine':
        return k * 9/5
    else:
        return k

def convertir_unidades(valor, de_unidad, a_unidad, diccionario):
    """Función universal para conversiones lineales"""
    valor_base = valor * diccionario[de_unidad]
    resultado = valor_base / diccionario[a_unidad]
    return resultado

SISTEMAS_LINEALES = {
    "Presión": DICCIONARIO_PRESION,
    "Masa": DICCIONARIO_MASA,
    "Longitud": DICCIONARIO_LONGITUD,
    "Volumen": DICCIONARIO_VOLUMEN,
    "Energía": DICCIONARIO_ENERGIA
}