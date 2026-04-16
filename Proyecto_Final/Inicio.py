# Menú principal para el usuario
Mascotas = []
    
print("="*50)
print("¡Tu nuevo mejor amigo te está esperando!")
print("="*50)   
print("Bienvenidos a nuestra comunidad. Aquí no solo adoptas una mascota, " )
print("salvas una vida y ganas un amor incondicional para siempre. Ya sea ")
print("que busques la energía de un perro o la compañía independiente de un ")
print("gato, estás en el lugar correcto para completar tu familia.")
print("\n      ¿Listo para conocerlos?      \n")

# Definiendo intereses


print("1 ¿Eres Team perros?")
print("2 ¿Eres Team gatos?")  
print("3 ¿te gustan ambos?")
print("")

# Creando mascotas de prueba
# Clase (nombre, edad_meses, tamaño, estado_salud)
Zeus = Perro("Zeus", 15, "Grande", "Sano")
Kaiser = Perro("Kaiser", 144, "Mediano", "Estable")
Mascotas.append(Zeus)
Mascotas.append(Kaiser)


while True:
    
    mascota_interes = int(input("Elige una opción (1, 2 o 3): "))
    if mascota_interes == 1: 
        # Recorrido por la  lista en linea 2
        for animal in Mascotas:
            # Verrerificacion de clase
            if isinstance(animal, Perro):
                print(f"{animal.nombre} (Edad: {animal.edad_meses} meses)")
                
                


