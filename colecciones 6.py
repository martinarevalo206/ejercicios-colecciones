# Ejercicio 1: Conversión de lista a tupla sin duplicados

# 1. Solicitamos al usuario una lista de elementos separados por espacio.
#    No usamos map aquí porque son textos, no números.
lista = input("Ingresa los elementos separados por espacio: ").split()

# 2. Convertimos la lista a un conjunto (set).
#    El set elimina automáticamente los elementos duplicados.
sin_duplicados = set(lista)

# 3. Convertimos el set nuevamente a una tupla.
tupla_final = tuple(sin_duplicados)

# 4. Mostramos el resultado final.
print("Tupla sin duplicados:", tupla_final)