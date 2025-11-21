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
