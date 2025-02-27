# Programa 1

def buscar_valor(matriz, valor):
  for i in range(len(matriz)):
      for j in range(len(matriz[i])):
          if matriz[i][j] == valor:
              return i, j
  return None

# Matriz 3x3
matriz = [
    [5, 8, 2],
    [1, 9, 4],
    [7, 6, 3]
]

# Valor a buscar en la matriz

valor_buscar = int(input("Ingrese el valor a buscar: "))

# Buscar el valor en la matriz

posicion = buscar_valor(matriz, valor_buscar)

# Mostrar el resultado

if posicion:
    print(f"El valor {valor_buscar} se encontró en la posición {posicion}.")
else:
    print(f"El valor {valor_buscar} no se encontró en la matriz.")
