# Programa que convierte un número decimal a binario

numero = int(input("Ingresa un número decimal: "))

binario = ""

if numero == 0:
    binario = "0"
else:
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2

print("El número en binario es:", binario)
