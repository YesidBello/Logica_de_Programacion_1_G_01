# Definicion de variables
datos = []
print("\n INGRESA DATOS POSITIVOS (para finalizar "
      "ingresa la palabra ¨fin¨)")
print(" ")
# Ciclo
while True:
    entrada = input("Ingresa un dato: ")
    if entrada.lower() == "fin":
        if len(datos) == 0:
            print(" ")
            print("¡ERROR! Debes ingresar al menos un dato antes"
                  " de finalizar")
            print(" ")
            continue
        else:
            break
    try:
        numero = float(entrada)
        if numero < 0:
            print(" ")
            print("¡ERROR! El número no puede ser negativo")
            print(" ")
            continue
        datos.append(numero)
    except ValueError:
        print("¡DATO INVÁLIDO! Por favor ingresa solo números")

# Proceso matematico
if len(datos) > 0:
    n = len(datos)
    promedio = sum(datos) / n

    suma_diferencias = 0
    for dato in datos:
        suma_diferencias = (dato - promedio) ** 2 + suma_diferencias
    desviacion_tipica = (suma_diferencias / n) ** 0.5
    print("\n              ---RESULTADOS---              \n")
    print("La desviación típica de los datos es: ", desviacion_tipica, "\n")
else:
    print("¡NO SE INGRESARON DATOS VÁLIDOS!")
