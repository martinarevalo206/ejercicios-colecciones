# Ejercicio 4: Diferencia simétrica entre dos conjuntos

# 1. Ingresamos los conjuntos en formato real con llaves.
A = eval(input("Ingresa el conjunto A (ej: {1, 2, 3}): "))
B = eval(input("Ingresa el conjunto B (ej: {3, 4, 5}): "))

# 2. Calculamos la diferencia simétrica.
#    Elementos que están en A o en B, pero no en ambos.
resultado = A ^ B     # También se puede usar A.symmetric_difference(B)

# 3. Mostramos el resultado.
print(resultado)