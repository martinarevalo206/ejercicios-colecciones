# Ejercicio 5: Transposición de una matriz
# split  separa el texto escrito por espacios y crea una lista de cadenas.
# map  convierte cada cadena en un número entero.

# 1. Solicitamos al usuario el tamaño de la matriz.
n = int(input("Ingresa el número de filas: "))
m = int(input("Ingresa el número de columnas: "))

# 2. Ingresamos la matriz original.
print("\nIngresa los elementos de la matriz (fila por fila y separados por espacios):")
matriz = []
for i in range(n):
    # Ingresamos una fila como números separados por espacio y los convertimos a enteros.
    fila = list(map(int, input(f"Fila {i+1}: ").split()))
    matriz.append(fila)

# 3. Creamos la matriz transpuesta.
#    La transpuesta cambia filas por columnas:
#    Si la original es n×m, la transpuesta será m×n.
transpuesta = []

for j in range(m):           # Recorre las columnas de la matriz original
    nueva_fila = []
    for i in range(n):       # Recorre las filas de la matriz original
        nueva_fila.append(matriz[i][j])  # Toma A[i][j] y lo convierte en A[j][i]
    transpuesta.append(nueva_fila)

# 4. Mostramos la matriz transpuesta.
print("\nLa matriz transpuesta es:")
for fila in transpuesta:
    print(fila)
