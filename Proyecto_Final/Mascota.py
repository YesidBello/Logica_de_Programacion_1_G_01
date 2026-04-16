class Adopcion:
    def __init__(self, nombre:str, edad:int, raza:str, salud:str)-> None:
        self.nombre =nombre_mascota 
        self.edad =edad_mascota
        self.raza =raza_mascota
        self.__salud =salud_mascota
        self.sonido =sonido_emitido
  

    def mostrar_informacion(self)-> str:
       return f"Nombre de la mascota es {self.nombre}, la edad que tiene te la mostraremos en meses y tiene {self.edad} meses,\n la raza a la cual pertenece es: {self.raza} y su estado de salud es: {self.salud}"
    
    def actualizar_salud(self, nsalud:str)-> None:
        self.__salud =nsalud

  

  

class Perro:
   def __init__(self, energia:str, sonido:str)-> None:
       self.energia =nivel_energia
       self.sonido =sonido_emitido
    
    def mostrar_informacion(self)-> str:
        return f"El nivel de energía de la mascota es: {self.energia} y el nivel de sonido que emite la mascota es: {self.sonido}"
  
class Gato:
    def __init__(self, independencia:str, sonido:str)-> None:
       self.independencia =nivel de independencia
       self.sonido =nivel_emitido
   
    def mostrar_informacion(self)-> str:   
        return f"El nivel de energía de la mascota es: {self.energia} y el nivel de independencia de la mascota es: {self.independencia}"
  

  

  

  

  

  
# Ejemplo de las respuestas que recibira el codigo
      
tipo = input("Ingrese el tipo de mascota (Perro/Gato): ")

if tipo.lower() == "perro":
    mascota1 = Perro("Sol", 18, "Pastor Alemán", "Excelente", "fuerte")
    print(mascota1.mostrar_informacion())


elif tipo.lower() == "gato":
    mascota1 = Gato("Luna", 5, "Siames", "Falta vacunas", "bajo")
    print(mascota1.mostrar_informacion())


  
    

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

