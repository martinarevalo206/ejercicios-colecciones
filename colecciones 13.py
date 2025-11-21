# Ejercicio 3: Intersección de números pares
# Usamos map(int, ...) para convertir los valores ingresados a enteros.
# split() separa por espacios.

# 1. Ingresamos la lista A
A = list(map(int, input("Ingresa la lista A (números separados por espacio): ").split()))

# 2. Ingresamos la lista B
B = list(map(int, input("Ingresa la lista B (números separados por espacio): ").split()))

# 3. Filtramos únicamente los números pares de cada lista
pares_A = {x for x in A if x % 2 == 0}
pares_B = {x for x in B if x % 2 == 0}

# 4. Calculamos la intersección de ambos conjuntos de pares
interseccion = pares_A & pares_B

# 5. Mostramos el resultado
print(interseccion)
