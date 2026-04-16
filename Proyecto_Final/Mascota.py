class Adopcion:
    def __init__(self, nombre:str, edad:int, raza:str, salud:str)-> None:
        self.nombre =nombre
        self.edad =edad
        self.raza =raza
        self.__salud =salud
        self.sonido =sonido
  

    def mostrar_informacion(self)-> str:
       return f"Nombre de la mascota es {self.nombre}, la edad que tiene te la mostraremos en meses y tiene {self.edad} meses,\n la raza a la cual pertenece es: {self.raza} y su estado de salud es: {self.salud}"
    
    def actualizar_salud(self, nsalud:str)-> None:
        self.__salud =nsalud

  

  

class Perro:
   def __init__(self, nombre:str, edad:int, raza:str, salud:str, energia:str, sonido:str)-> None:
    super().__init__(nombre, edad, raza, salud, energia, sonido)
# Hace que la información de class Adopcion pasen a esta class y no se repita todo, tambien hace que se puede hacer la herencia.
       self.energia =energia
       self.sonido =sonido
    
    def mostrar_informacion(self)-> str:
        return  super().mostrar_informacion() + f", el nivel de la energía de la mascota es: {self.energia} y el nivel de sonido es: {self.sonido}"
# Se disminuye la inscripcion inecesaria al juntar el super y sumarlo con los datos que nos dan en esta class.
  
class Gato:
    def __init__(self, nombre:str, edad:int, raza:str, salud:str, independencia:str, sonido:str)-> None:
       self.independencia =independencia
       self.sonido =sonido
   
    def mostrar_informacion(self)-> str:   
        return super().mostrar_informacion() + f", el nivel de independencia de la mascota es: {self.independencia} y el nivel de sonido es: {self.sonido}"

  

  

  

  

  
# Ejemplo de las respuestas que recibira el codigo
      
tipo = input("Ingrese el tipo de mascota (Perro/Gato): ")

if tipo.lower() == "perro":
    mascota1 = Perro("Sol", 18, "Pastor Alemán", "Excelente","alta", "fuerte")
    print(mascota1.mostrar_informacion())


elif tipo.lower() == "gato":
    mascota1 = Gato("Luna", 5, "Siames", "Falta vacunas", "media", "bajo")
    print(mascota1.mostrar_informacion())


  
    

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

