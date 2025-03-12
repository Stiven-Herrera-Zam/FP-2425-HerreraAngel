def calcular_temperatura_promedio(datos_temperaturas):
    """
    #ESTA FUNCIÓN CALCULA LA TEMPERATURA PROMEDIO DE UN CONJUNTO DE CIUDADES

    :param datos_temperaturas:   Diccionario con las temperaturas de cada ciudad
    :return:                     Diccionario con las temperaturas promedio de cada ciudad
    """
    promedios = {}
    for ciudad, temperaturas in datos_temperaturas.items():
        promedio_ciudad = sum(temperaturas) / len(temperaturas)
        promedios[ciudad] = promedio_ciudad
    return promedios

#TEMPERATURAS 3 CIUDADES EN 4 SEMANAS

datos_temperaturas = {
   "Guayaquil": [88, 76, 85, 78],
   "Portoviejo": [62, 66, 68, 80],
    "Quito": [20, 52, 39, 63]
}

# LLAMAMOS A LA FUNCIÓN PARA CALCULAR LAS TEMPERATURAS PROMEDIOS
temperaturas_promedio = calcular_temperatura_promedio(datos_temperaturas)

# MOSTRAMOS LOS RESULTADOS
print("Temperaturas promedio por ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {promedio: .2f}°c")

