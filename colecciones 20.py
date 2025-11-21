 Ejercicio 5: Fusionar diccionarios
# Diccionarios iniciales
A = {'x': 1, 'y': 2}
B = {'y': 10, 'z': 3}

# Para fusionar diccionarios tenemos dos opciones principales:

# Opción 1: Usar update()
# .update() modifica el diccionario A directamente
# y si una clave se repite, el valor de B sobreescribe el de A.
fusion1 = A.copy()   # Usamos copy() para no modificar A original
fusion1.update(B)

# Opción 2: Usar el operador |
# Este operador crea un nuevo diccionario sin modificar los originales.
fusion2 = A | B

# Mostrar resultados
print("Usando update():", fusion1)
print("Usando operador | :", fusion2)
