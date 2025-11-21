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
