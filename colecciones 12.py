# Ejercicio 2: Palabras únicas de una frase

# 1. Solicitamos la frase al usuario.
frase = input("Ingresa una frase: ")

# 2. Separamos la frase en palabras usando split().
#    Esto genera una lista como ["hola", "mundo", "hola", "python"]
palabras = frase.split()

# 3. Convertimos la lista en un set para eliminar duplicados.
palabras_unicas = set(palabras)

# 4. Mostramos el conjunto resultante.
print(palabras_unicas)