# Definicion de variables
datos = []
print("\n INGRESA NUMEROS ENTEROS POSITIVOS (para finalizar "
      "ingresa la palabra ¨fin¨)")

# Ciclo
while True:
    entrada = input("Ingresa un número: ")
    if entrada.lower() == "fin":
        if len(datos) == 0:
            print("\n ¡ERROR! Debes ingresar al menos un número "
                  "para finalizar")
            continue
        else:
            break
    try:
        numero = int(entrada)
        if numero <= 0:
            print("\n ¡ERROR! El número debe ser mayor a 0 \n")
            continue
        datos.append(numero)
    except ValueError:
        print("\n !NO SE INGRESARON NÚMEROS VÁLIDOS! por favor ingresa solo"
              " números enteros (sin puntos) \n")
print("\n               ---RESULTADOS---               \n")


# Proceso matematico
if len(datos) > 0:
    for dato in datos:
        raiz_cuadrada = (dato**0.5)
        cuadrado = (dato**2)
        cubo = (dato**3)
        print("Para el número:", dato)
        print("         La raíz cuadrada es:", round(raiz_cuadrada, 4))
        print("         El cuadrado es:", cuadrado)
        print("         El cubo es:", cubo)
        print("------------------------------------------------""\n")
