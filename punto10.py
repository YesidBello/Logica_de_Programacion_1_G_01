

M = int(input("Ingresa un número entero positivo: "))

suma_primos = 0
cantidad_primos = 0

print("Números primos hasta", M, ":")

for num in range(2, M + 1):
    es_primo = True

    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break

    if es_primo:
        print(num)
        suma_primos += num
        cantidad_primos += 1

print("Suma de los números primos:", suma_primos)
print("Cantidad de números primos:", cantidad_primos)