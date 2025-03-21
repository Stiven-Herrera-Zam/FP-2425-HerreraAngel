# Definición de una función con parámetros

def calcular_descuento(monto_total, descuento = 10):
    """

    :param monto_total:
    :param descuento:
    :return:
    """
    descuento = (monto_total * descuento) / 100
    return descuento

# Llamada a la función

monto1 = 1500
monto2 = 2305
porcentaje_personalizado = 20

# Primera llamada con el porcentaje 10%

descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

# Segunda llamada con el porcentaje 20%

descuento2 = calcular_descuento(monto2, porcentaje_personalizado)
monto_final2 = monto2 - descuento2

# Mostrar resultados

print(f"compra 1: Monto total: {monto1}, Descuento: {descuento1}, Monto final: {monto_final1}")
print(f"Compra 2: Monto total: {monto2}, Descuento: {descuento2}, Monto final: {monto_final2}")

