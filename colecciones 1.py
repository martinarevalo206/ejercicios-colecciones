# Ejercicio 1: Números mayores que el promedio

# 1. Pedimos al usuario una lista de números en una sola línea.
#    Usamos split() para separar por espacios y map() para convertir a enteros.
numeros = list(map(int, input("Ingresa una lista de números separados por espacio: ").split()))

# 2. Calculamos el promedio: suma de los elementos / cantidad de elementos.
promedio = sum(numeros) / len(numeros)

# 3. Filtramos los números que sean estrictamente mayores al promedio.
mayores = [n for n in numeros if n > promedio]

# 4. Mostramos resultados.
print(f"Promedio: {promedio}")
print(f"Mayores que el promedio: {sorted(mayores)}")  # sorted para orden ascendente
