# Ejercicio 1: Unión y diferencia entre conjuntos

# 1. Ingresamos los conjuntos usando formato real con llaves { }.
#    Se usa eval() porque el formato del ejercicio es controlado.
A = eval(input("Ingresa el conjunto A (ej: {1, 2, 3}): "))
B = eval(input("Ingresa el conjunto B (ej: {3, 4, 5}): "))

# 2. Calculamos la unión A | B
union = A | B

# 3. Calculamos la diferencia A - B
diferencia = A - B

# 4. Mostramos los resultados
print(f"Unión: {union}")
print(f"Diferencia: {diferencia}")
