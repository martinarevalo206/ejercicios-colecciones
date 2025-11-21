# Ejercicio 4: Suma de dos matrices

# 1. Primero pedimos el tamaño de la matriz (n filas, m columnas)
n = int(input("Ingresa el número de filas: "))
m = int(input("Ingresa el número de columnas: "))

# 2. Ingresamos la matriz A
print("\nIngresa los elementos de la matriz A (Separados por espacios):")
A = []
for i in range(n):
    # El método split() divide un texto en partes separadas por espacios.
    # La función map() aplica la conversión int a cada una de esas partes.
    fila = list(map(int, input(f"Fila {i+1}: ").split()))
    A.append(fila)

# 3. Ingresamos la matriz B
print("\nIngresa los elementos de la matriz B (Separados por espacios):")
B = []
for i in range(n):
    # split  separa el texto escrito por espacios y crea una lista de cadenas.
    # map  convierte cada cadena en un número entero.
    fila = list(map(int, input(f"Fila {i+1}: ").split()))
    B.append(fila)

# 4. Calculamos la suma de las matrices.
#    La suma es elemento a elemento:
#    C[i][j] = A[i][j] + B[i][j]
C = []
for i in range(n):
    fila_suma = []
    for j in range(m):
        fila_suma.append(A[i][j] + B[i][j])
    C.append(fila_suma)

# 5. Mostramos la matriz resultante
print("\nLa matriz suma es:")
for fila in C:
    print(fila)