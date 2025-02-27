def index(matriz, valor_buscado):
    # Recorrer cada fila de la matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return (i, j)  # Retornar la posición (fila, columna) si se encuentra el valor
    return None  # Retornar None si el valor no se encuentra

def print_matrix(matriz):
    for row in matriz:
        print(row)

# Definir una matriz 3x3 con valores numéricos diferentes
matriz = [
    [12, 34, 56],
    [78, 90, 23],
    [45, 67, 89]
]

print("Matriz:")
print_matrix(matriz)

# Valor a buscar
valor_a_buscar = 90

# Buscar el valor en la matriz
resultado = index(matriz, valor_a_buscar)

# Imprimir la posición buscada y el resultado
if resultado is not None:
    print(f"\nBuscando el valor {valor_a_buscar}...")
    print(f" En la posición : {resultado} se encuentra el valor {valor_a_buscar}")
else:
    print(f"\nBuscando el valor {valor_a_buscar}...")
    print(f"El valor {valor_a_buscar} no se encuentra en la matriz.")