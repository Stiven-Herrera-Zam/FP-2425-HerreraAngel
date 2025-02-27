# Programa 2
def bubble_sort(arr):
    """Función que implementa el algoritmo Bubble sort para ordenadores una lista."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def ordenar_fila(matriz, fila):
    """Ordena una fila específica de la matriz en orden ascendente."""
    if 0 <= fila < len (matriz):  # Verificar que la fila exista
        bubble_sort(matriz[fila])  # Ordenar la fila específica
    else:
        print(" El Número de fila inválido.")

# Matriz 3x3 con valores numéricos

matriz = [
    [9, 5, 3],
    [8, 6, 7],
    [2, 4, 1],
]

# Mostrar matriz original

print("Matriz original")
for fila in matriz:
    print(fila)

# Seleccionar la fila ordenada

fila_a_ordenar = int(input("Ingrese el número de fila a ordenar (0-2): "))

# Ordenar la fila seleccionada
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada

print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)





