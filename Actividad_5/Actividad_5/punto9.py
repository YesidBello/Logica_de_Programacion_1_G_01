num = int(input("Ingrese un número decimal: "))
binario = ""

if num == 0:
    binario = "0"
else:
    while num > 0:
        residuo = num % 2
        binario = str(residuo) + binario
        num = num // 2

print("El número en binario es:", binario)
