N = int(input("¿Cuántos estudiantes hay?: "))
suma = 0
aprobados = 0
reprobados = 0
nota = float(input("Ingresa la nota del estudiante 1 (de 1 a 10): "))
suma += nota

if nota >= 7:
    aprobados += 1
else:
    reprobados += 1

mayor = nota
menor = nota
for i in range(2, N + 1):
    nota = float(input("Ingresa la nota del estudiante " + str(i) + " (de 1 a 10): "))
    xsuma += nota

    if nota >= 7:
        aprobados += 1
    else:
        reprobados += 1

    if nota > mayor:
        mayor = nota

    if nota < menor:
        menor = nota

promedio = suma / N

print("\nResultados:")
print("Promedio de las notas:", promedio)
print("Cantidad de estudiantes aprobados:", aprobados)
print("Cantidad de estudiantes reprobados:", reprobados)
print("Nota más alta:", mayor)
print("Nota más baja:", menor)

