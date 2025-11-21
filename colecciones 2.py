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