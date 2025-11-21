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
