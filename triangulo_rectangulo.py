from itertools import combinations

def contar_triangulos(conjunto):
    conjuntos = 0
    for x, y, z in combinations(conjunto, 3):
        lados = sorted([x, y, z])
        a, b, c = lados
        if a**2 + b**2 == c**2:
            conjuntos += 1
    return conjuntos

entrada = input("Ingrese los conjuntos de números, el programa tendra en cuenta ternas de forma sucesiva, verifica que este bien su orden: ")
datos = list(map(int, entrada .split()))
resultado = contar_triangulos(datos)
if resultado > 0:
    print(f"Sí hay triángulos rectángulos y son {resultado}")
else:
    print("No hay ninguno")