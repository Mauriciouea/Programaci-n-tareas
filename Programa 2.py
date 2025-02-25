def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambiar si el elemento encontrado es mayor que el siguiente
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def ordenar_fila(matriz, fila):
    if fila < 0 or fila >= len(matriz):
        print("Índice de fila fuera de rango.")
        return

    # Llamar a la función de ordenación en la fila especificada
    bubble_sort(matriz[fila])

# definir matriz
matriz = [
    [3, 1, 2],
    [6, 4, 5],
    [9, 7, 8]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila 0 (segunda fila)
ordenar_fila(matriz, 0)

print("\nMatriz después de ordenar la fila 0:")
for fila in matriz:
    print(fila)

# Ordenar la fila 1 (segunda fila)
ordenar_fila(matriz, 1)

print("\nMatriz después de ordenar la fila 1:")
for fila in matriz:
    print(fila)

# Ordenar la fila 2 (segunda fila)
ordenar_fila(matriz, 2)

print("\nMatriz después de ordenar la fila 2:")
for fila in matriz:
    print(fila)