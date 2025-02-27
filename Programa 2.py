def bubble_sort(arr):
    n = len(arr)
    # Recorrer todos los elementos de la matriz
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Cambiar si el elemento encontrado es mayor que el siguiente
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def sort_row(matrix, row_index):
    if row_index < 0 or row_index >= len(matrix):
        print("Índice de fila fuera de rango.")
        return
    # Llamar a la función de ordenación para la fila específica
    bubble_sort(matrix[row_index])

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Definir una matriz 3x3
matrix = [
    [9, 2, 5],
    [3, 8, 1],
    [4, 7, 6]
]

print("Matriz original:")
print_matrix(matrix)

# Ordenar la fila 1 (segunda fila)
sort_row(matrix, 1)

print("\nMatriz después de ordenar la fila 1:")
print_matrix(matrix)