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
