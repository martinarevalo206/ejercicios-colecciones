# Ejercicio 2: Contador de palabras
# Solicitamos la frase al usuario
frase = input("Ingresa una frase: ")

# Dividimos la frase en palabras usando split()
palabras = frase.split()

# Creamos un diccionario vacío que contendrá el conteo
contador = {}

# Recorremos cada palabra de la lista
for palabra in palabras:
    # Si la palabra ya está en el diccionario, aumentamos su contador
    if palabra in contador:
        contador[palabra] += 1
    else:
        # Si no está, se agrega con valor inicial 1
        contador[palabra] = 1

# Mostramos el diccionario con el conteo final
print(contador)
