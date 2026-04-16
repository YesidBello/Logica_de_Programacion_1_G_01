# Definicion de variables
datos = []
print("\n INGRESA NÚMEROS POSITIVOS (para finalizar ingresa "
      "la palabra ¨fin¨)")

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
        numero = float(entrada)
        if numero < 0:
            print("\n ¡ERROR! El número debe ser "
                  "mayor a cero \n ")
            continue
        datos.append(numero)
    except ValueError:
        print("\n !NO SE INGRESARON DIGITOS VÁLIDOS! por favor ingresa solo"
              " números \n")
        
# Proceso matematico
triangulos_rectangulos = []
for z in range(0, len(datos) - 2, 3):
    lado_a = datos[z]
    lado_b = datos[z + 1]
    lado_c = datos[z + 2]

    terna = [lado_a, lado_b, lado_c]
    terna.sort()

    cateto_1 = terna[0]
    cateto_2 = terna[1]
    hipotenusa = terna[2]
    
    if hipotenusa**2 == (cateto_1**2 + cateto_2**2):
        triangulos_rectangulos.append(terna)
        
print("\n            ---RESULTADOS---            \n")
print("Ternas válidas evaluadas: ", len(datos) // 3)
    
cantidad_triangulos = len(triangulos_rectangulos)
print("Cantidad de triangulos rectangulos: ", cantidad_triangulos)

if cantidad_triangulos > 0:
    print("Los números que forman los triangulos son: ")
    for triangulo in triangulos_rectangulos:
        print(f"- catetos: {triangulo[0]} y {triangulo[1]}")
        print(f"- hipotenusa: {triangulo[2]}")
        print("-------------------------------------------------")
        
          



     
        