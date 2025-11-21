# Ejercicio 4: Diccionario invertido
# Diccionario original
diccionario = {'a': 1, 'b': 2, 'c': 3}

# Invertimos el diccionario
# .items() devuelve pares (clave, valor)
# La comprensión crea un nuevo diccionario donde cada valor pasa a ser clave
diccionario_invertido = {valor: clave for clave, valor in diccionario.items()}

# Mostramos el resultado
print("Diccionario invertido:", diccionario_invertido)