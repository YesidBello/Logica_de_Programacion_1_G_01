a = float(input("Ingresa el peso de la esfera A: "))
b = float(input("Ingresa el peso de la esfera B: "))
c = float(input("Ingresa el peso de la esfera C: "))

print("\n--- Resultado ---")
if a > b:
    if a > c:
        print("La esfera A es la de mayor peso.")
    else:
        print("La esfera C es la de mayor peso.")
else:
    if b > c:
        print("La esfera B es la de mayor peso.")
    else:
        print("La esfera C es la de mayor peso.")