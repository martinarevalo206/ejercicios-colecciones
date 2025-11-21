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
