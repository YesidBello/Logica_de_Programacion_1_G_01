# Definición de variables
datos = []
print("\n INGRESA VALORES POSITIVOS (para finalizar "
      "ingresa la palabra ¨fin¨)")

# Ciclo
while True:
    entrada = input("Ingresa un número: ")
    if entrada.lower() == "fin":
        if len(datos) == 0:
            print("\n ¡ERROR! Debes ingresar al menos un número"
                  " para finalizar")
        else:
            break
    try:
        numero = float(entrada)
        if numero < 0:
            print("\n ¡ERROR! El número debe ser mayor a 0 \n")
            continue
        datos.append(numero)
    except ValueError:
        print("\n !NO SE INGRESARON VALORES VÁLIDOS! por favor ingresa solo"
              " números \n")

# proceso matematico
maximo = datos[0]
minimo = datos[0]
for dato in datos:
    if dato > maximo:
        maximo = dato
    if dato < minimo:
        minimo = dato
suma_maxmin = maximo + minimo
print("\n               ---RESULTADO---          \n")
print("    El número máximo es: ", maximo)
print("    El número minímo es: ", minimo)
print("    La suma de ambos es: ", suma_maxmin)
print(" ")
