# -*- coding: utf-8 -*-


"""
# **EJERCICIOS EN PYTHON**

#  **LISTAS Y MATRICES**
"""

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

# Ejercicio 2: Producto escalar de dos listas

# 1. Solicitamos dos listas al usuario como texto
entrada_a = input("Ingresa la Lista A (números separados por espacio): ")
entrada_b = input("Ingresa la Lista B (números separados por espacio): ")

# 2. Convertimos cada elemento a entero
lista_a = []
for elemento in entrada_a.split():
    lista_a.append(int(elemento))  # Convertimos cada string a entero y lo agregamos manualmente

lista_b = []
for elemento in entrada_b.split():
    lista_b.append(int(elemento))

# 3. Verificamos que tengan el mismo tamaño
if len(lista_a) != len(lista_b):
    print("Error: Las dos listas deben tener el mismo tamaño.")
else:
    # 4. Calculamos el producto escalar
    producto_escalar = 0

    for i in range(len(lista_a)):
        multiplicacion = lista_a[i] * lista_b[i]  # Multiplicamos los elementos en la misma posición
        producto_escalar += multiplicacion        # Sumamos al acumulador

    # 5. Mostramos el resultado final
    print(f"Producto escalar = {producto_escalar}")

# Ejercicio 3: Matriz identidad

# 1. Solicitamos el tamaño n de la matriz identidad.
n = int(input("Ingresa el valor de n para construir una matriz identidad n×n: "))

# 2. Creamos la matriz identidad.
matriz_identidad = []

for i in range(n):  # Recorre cada fila
    fila = []
    for j in range(n):  # Recorre cada columna
        if i == j:
            fila.append(1)   # En la diagonal principal
        else:
            fila.append(0)   # Fuera de la diagonal
    matriz_identidad.append(fila)

# 3. Imprimimos la matriz identidad.
for fila in matriz_identidad:
    print(fila)

# Ejercicio 4: Suma de dos matrices

# 1. Primero pedimos el tamaño de la matriz (n filas, m columnas)
n = int(input("Ingresa el número de filas: "))
m = int(input("Ingresa el número de columnas: "))

# 2. Ingresamos la matriz A
print("\nIngresa los elementos de la matriz A (Separados por espacios):")
A = []
for i in range(n):
    # El método split() divide un texto en partes separadas por espacios.
    # La función map() aplica la conversión int a cada una de esas partes.
    fila = list(map(int, input(f"Fila {i+1}: ").split()))
    A.append(fila)

# 3. Ingresamos la matriz B
print("\nIngresa los elementos de la matriz B (Separados por espacios):")
B = []
for i in range(n):
    # split  separa el texto escrito por espacios y crea una lista de cadenas.
    # map  convierte cada cadena en un número entero.
    fila = list(map(int, input(f"Fila {i+1}: ").split()))
    B.append(fila)

# 4. Calculamos la suma de las matrices.
#    La suma es elemento a elemento:
#    C[i][j] = A[i][j] + B[i][j]
C = []
for i in range(n):
    fila_suma = []
    for j in range(m):
        fila_suma.append(A[i][j] + B[i][j])
    C.append(fila_suma)

# 5. Mostramos la matriz resultante
print("\nLa matriz suma es:")
for fila in C:
    print(fila)

# Ejercicio 5: Transposición de una matriz
# split  separa el texto escrito por espacios y crea una lista de cadenas.
# map  convierte cada cadena en un número entero.

# 1. Solicitamos al usuario el tamaño de la matriz.
n = int(input("Ingresa el número de filas: "))
m = int(input("Ingresa el número de columnas: "))

# 2. Ingresamos la matriz original.
print("\nIngresa los elementos de la matriz (fila por fila y separados por espacios):")
matriz = []
for i in range(n):
    # Ingresamos una fila como números separados por espacio y los convertimos a enteros.
    fila = list(map(int, input(f"Fila {i+1}: ").split()))
    matriz.append(fila)

# 3. Creamos la matriz transpuesta.
#    La transpuesta cambia filas por columnas:
#    Si la original es n×m, la transpuesta será m×n.
transpuesta = []

for j in range(m):           # Recorre las columnas de la matriz original
    nueva_fila = []
    for i in range(n):       # Recorre las filas de la matriz original
        nueva_fila.append(matriz[i][j])  # Toma A[i][j] y lo convierte en A[j][i]
    transpuesta.append(nueva_fila)

# 4. Mostramos la matriz transpuesta.
print("\nLa matriz transpuesta es:")
for fila in transpuesta:
    print(fila)

"""

#   **TUPLAS**

"""

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

# Ejercicio 2: Coordenadas dentro de un rango

# 1. Solicitamos al usuario las coordenadas (x, y).
#    Usamos map(int, ...) para convertir los valores ingresados a enteros.
x, y = map(int, input("Ingresa la coordenada (x y): ").split())

# 2. Solicitamos los límites del rango.
#    El rango se interpreta como un intervalo cerrado: [min_rango, max_rango]
min_rango = int(input("Ingresa el límite inferior del rango: "))
max_rango = int(input("Ingresa el límite superior del rango: "))

# 3. Verificamos si x y y están dentro del rango.
#    La condición es que ambos valores estén entre min_rango y max_rango.
if min_rango <= x <= max_rango and min_rango <= y <= max_rango:
    print("Dentro del rango")
else:
    print("Fuera del rango")

# Ejercicio 3: Empaquetar y desempaquetar datos

# 1. Ingresamos los datos del usuario.
#    split() separa por espacios. La edad se convierte después a entero.
nombre = input("Ingresa el nombre: ")
edad = int(input("Ingresa la edad: "))
pais = input("Ingresa el país: ")

# 2. Empaquetamos los datos en una tupla.
datos = (nombre, edad, pais)

# 3. Desempaquetamos la tupla asignando cada elemento a una variable.
nombre_des, edad_des, pais_des = datos

# 4. Mostramos los datos desempaquetados.
print("\nDatos desempaquetados:")
print(f"Nombre: {nombre_des}")
print(f"Edad: {edad_des}")
print(f"País: {pais_des}")

# Ejercicio 4: Comparación de dos tuplas numéricas

# 1. Ingresamos las tuplas en formato real.
#    Usamos eval() para convertir el texto "(3, 4, 5)" en una tupla real.
tupla1 = eval(input("Ingresa la primera tupla (ej: 3, 4, 5): "))
tupla2 = eval(input("Ingresa la segunda tupla (ej: 3, 4, 2): "))

# 2. Comparamos las tuplas
#    Python compara elemento por elemento:
#    (3,4,5) > (3,4,2) porque al llegar al tercer elemento 5 > 2.
if tupla1 > tupla2:
    print("La primera tupla es mayor.")
elif tupla1 < tupla2:
    print("La segunda tupla es mayor.")
else:
    print("Las dos tuplas son iguales.")

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

"""# **SETS**"""

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

# Ejercicio 4: Diferencia simétrica entre dos conjuntos

# 1. Ingresamos los conjuntos en formato real con llaves.
A = eval(input("Ingresa el conjunto A (ej: {1, 2, 3}): "))
B = eval(input("Ingresa el conjunto B (ej: {3, 4, 5}): "))

# 2. Calculamos la diferencia simétrica.
#    Elementos que están en A o en B, pero no en ambos.
resultado = A ^ B     # También se puede usar A.symmetric_difference(B)

# 3. Mostramos el resultado.
print(resultado)

# Ejercicio 5: Subconjunto y superconjunto

# 1. Ingresamos los conjuntos A y B en formato real usando llaves.
A = eval(input("Ingresa el conjunto A (ej: {1, 2}): "))
B = eval(input("Ingresa el conjunto B (ej: {1, 2, 3, 4}): "))

# 2. Verificamos si A es subconjunto de B.
#    - A.issubset(B) devuelve True si TODOS los elementos de A están dentro de B.
#    - Ejemplo: {1,2}.issubset({1,2,3}) = True
if A.issubset(B):
    print("A es subconjunto de B")

# 3. Verificamos si B es superconjunto de A.
#    - B.issuperset(A) devuelve True si B contiene TODOS los elementos de A.
#    - Es básicamente la condición inversa a issubset().
#    - Ejemplo: {1,2,3}.issuperset({1,2}) = True
if B.issuperset(A):
    print("B es superconjunto de A")

"""# **DICCIONARIOS**"""

# Ejercicio 1: Agenda telefónica
# Creamos un diccionario vacío donde guardaremos los contactos
agenda = {}

print("=== Agenda Telefónica ===")
print("Escribe 'fin' como nombre para terminar.\n")

while True:
    # Solicitamos el nombre
    nombre = input("Ingresa un nombre: ")

    # Usamos lower() para convertir el texto a minúsculas,
    # así podemos comparar sin importar si el usuario escribe FIN, Fin, fIn, etc.
    if nombre.lower() == "fin":
        break

    # Solicitamos el teléfono asociado
    telefono = input("Ingresa el teléfono: ")

    # Guardamos en el diccionario: clave = nombre, valor = teléfono
    agenda[nombre] = telefono
    print("Contacto agregado.\n")

# Mostramos el diccionario final
print("\n=== Agenda Final ===")
print(agenda)

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

# Ejercicio 3: Promedio de calificaciones
# Creamos un diccionario vacío para almacenar nombre → nota
calificaciones = {}

print("Ingresa el nombre y la nota ej: Ana: 2.5 (escribe 'fin' para terminar):")

while True:
    entrada = input("> ")

    # Si el usuario escribe "fin", se detiene el ingreso
    if entrada.lower() == "fin":
        break

    # Esperamos el formato: Nombre: Nota
    # Ejemplo: Ana: 4.0
    try:
        nombre, nota = entrada.split(":")
        nombre = nombre.strip()
        nota = float(nota.strip())
        calificaciones[nombre] = nota
    except:
        print("Formato inválido. Usa: Nombre: Nota")
        continue

# Obtenemos solo las notas usando .values()
notas = calificaciones.values()

# Calculamos el promedio usando sum() y len()
promedio = sum(notas) / len(notas) if len(notas) > 0 else 0

# Mostramos el resultado final
print(f"Promedio general: {promedio}")

# Ejercicio 4: Diccionario invertido
# Diccionario original
diccionario = {'a': 1, 'b': 2, 'c': 3}

# Invertimos el diccionario
# .items() devuelve pares (clave, valor)
# La comprensión crea un nuevo diccionario donde cada valor pasa a ser clave
diccionario_invertido = {valor: clave for clave, valor in diccionario.items()}

# Mostramos el resultado
print("Diccionario invertido:", diccionario_invertido)

# Ejercicio 5: Fusionar diccionarios
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