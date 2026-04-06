# Definicion de variables
suma_impares = 0
contador = 1


# Ciclo
while True:
    try:
        N = int(input("Escribe un número entero positivo: "))
        if N > 0:
            break
        else:
            print("\n ¡ERROR! El número debe ser mayor a 0 \n")
    except ValueError:
        print("\n ¡NÚMERO INVÁLIDO! Ingresa solo números enteros \n")

# Proceso matematico
while contador <= N:
    if contador % 2 != 0:
        suma_impares = suma_impares + contador
    contador = contador + 1
print("\n       ---RESULTADO---        \n")
print("La suma de números impares es: ", suma_impares, "\n")
