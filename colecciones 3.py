# Ejercicio 3: Matriz identidad

# 1. Solicitamos el tamaño n de la matriz identidad.
n = int(input("Ingresa el valor de n para construir una matriz identidad n×n: "))

# 2. Creamos la matriz identidad.
matriz_identidad = []

for i in range(n):  # Recorre cada fila
    fila = []
    for j in range(n):  # Recorre cada columna
        if i == j:
            fila.append(1)   # En la diagonal principal
        else:
            fila.append(0)   # Fuera de la diagonal
    matriz_identidad.append(fila)

# 3. Imprimimos la matriz identidad.
for fila in matriz_identidad:
    print(fila)
