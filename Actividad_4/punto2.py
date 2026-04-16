a = float(input("Ingresa el peso de la esfera A: "))
b = float(input("Ingresa el peso de la esfera B: "))
c = float(input("Ingresa el peso de la esfera C: "))
d = float(input("Ingresa el peso de la esfera D: "))
print("\n---Resultado---")
if a == b:
    if a == c:
        if d > a:
            print("La esfera diferente es D y tiene mayor peso")
        else:
            print("La esfera diferente es D y tiene menor peso")
    else:
        if c > a:
            print("La esfera diferente es C y tiene mayor peso")
        else:
            print("La esfera diferente es C y tiene menor peso")
else:
    if a == d:
        if b > a:
            print("La esfera diferente es B y tiene mayor peso")
        else:
            print("La esfera diferente es B y tiene menor peso")
    if a > c:
        print("La esfera diferente es A y tiene mayor peso")
    else:
        print("La esfera diferente es A y tiene menor peso")
