from itertools import combinations
# Es como una bibloteca que añadimos para el problema
def contar_triangulos(conjunto):
    conjuntos = 0
    for x, y, z in combinations(conjunto, 3):
# Esta parte hace que se separen grupos de ha 3 para hacer las ternas
        lados = sorted([x, y, z])
# Sorted hace que la z sea la mayor y haci poder hacer el teorema de pitagoras, ya que seria la hipotenusa
        a, b, c = lados
        if a**2 + b**2 == c**2:
            conjuntos += 1
    return conjuntos

entrada = input("Ingrese los conjuntos de números, el programa tendra en cuenta ternas de forma sucesiva, verifica que este bien su orden: ")
datos = list(map(int, entrada .split()))
#entrada.split hace que los numeros se saparen por los espacios, map hace que todos reciban las indicaciones, int hace que se vuelvan enteros y list que sean listas.
resultado = contar_triangulos(datos)
# Es ver los datos de lo que se metio como conjuntos.
if resultado > 0:
    print(f"Sí hay triángulos rectángulos y son {resultado}")
else:
    print("No hay ninguno")