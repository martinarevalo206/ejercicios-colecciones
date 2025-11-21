# Ejercicio 5: Suma y promedio con tuplas

# 1. Ingresamos la tupla desde el usuario.
#    Se convierte a enteros con map().
tupla = tuple(map(int, input("Ingresa los números de la tupla (separados por espacio): ").split()))

# 2. Calculamos la suma usando sum().
suma = sum(tupla)

# 3. Calculamos el promedio usando sum() / len().
promedio = suma / len(tupla)

# 4. Mostramos los resultados.
print(f"Suma = {suma}")
print(f"Promedio = {promedio}")
