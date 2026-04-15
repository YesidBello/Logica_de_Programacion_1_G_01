nivel = input("Ingresa el nivel del estudiante (Pregrado o Posgrado): ").strip().lower()
promedio = float(input("Ingresa el promedio académico: "))

creditos = 0
descuento = 0.0
valor_credito = 0

print("\n--- Resultado ---")

if nivel == "pregrado":
    valor_credito = 50000
    if promedio >= 4.5:
        creditos = 28
        descuento = 0.25
    elif promedio >= 4.0:
        creditos = 25
        descuento = 0.10
    elif promedio > 3.5:
        creditos = 20
        descuento = 0.0
    elif promedio >= 2.5:
        creditos = 15
        descuento = 0.0
    else:
        print("Promedio muy bajo. No podrá matricularse.")
        
elif nivel == "posgrado":
    valor_credito = 300000
    if promedio >= 4.5:
        creditos = 20
        descuento = 0.20
    else:
        creditos = 10
        descuento = 0.0
else:
    print("Nivel de estudio no reconocido.")
if creditos > 0:
    subtotal = creditos * valor_credito
    total_a_pagar = subtotal - (subtotal * descuento)
    print(f"Créditos a registrar: {creditos}")
    print(f"Total a pagar: ${total_a_pagar:,.2f}")