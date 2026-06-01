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
        'Pascal': 1,
        'Atmósfera': 101325,
        'Bar': 100000,
        'PSI': 6894.76,
        'Milímetros de mercurio': 133.322
    }
    
    # Lógica: Convertir a Pa y luego dividir por el factor de la unidad destino
    valor_en_pa = valor * factores_pa[de_unidad]
    resultado = valor_en_pa / factores_pa[a_unidad]
    return resultado

DICCIONARIO_MASA = {
    'Kilogramo (kg)': 1.0,
    'Gramo (g)': 0.001,
    'Miligramo (mg)': 0.000001,
    'Libra (lb)': 0.45359237,      # 1 lb = 0.4535... kg
    'Onza (oz)': 0.0283495237,    # 1 oz = 0.0283... kg
    'Tonelada (t)': 1000.0
}

def convertir_masa(valor, de_unidad, a_unidad):
    # Convertimos a la base (kg) y luego a la unidad destino
    valor_en_kg = valor * DICCIONARIO_MASA[de_unidad]
    resultado = valor_en_kg / DICCIONARIO_MASA[a_unidad]
    return resultado