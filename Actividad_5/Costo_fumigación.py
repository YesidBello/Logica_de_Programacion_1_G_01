nombre = input('Ingrese su nombre: ')
hectarias = int(input('Ingrese el total de hectarias que se fumigarán: '))
print('Tenemos 4 tipos de fumigación: Tipo1 contra malas hierbas, tipo2 contra langostas, tipo3 contra gusanos y tipo4 todas las anteriores')
print('El tipo 1 tiene un precio de 10 dólares, el tipo 2 de 15 dólares, tipo 3 de 20 dólares y el tipo 4 de 30, estos precios son por una hectaria')

tipo_fumigacion = int(input('Ingresa el número del tipo de fumigación que quieras (1, 2, 3 o 4): '))

if tipo_fumigacion == 1:
    hectarias_tipo = hectarias * 10
elif tipo_fumigacion == 2:
    hectarias_tipo = hectarias * 15
elif tipo_fumigacion == 3:
    hectarias_tipo = hectarias * 20
else:
    hectarias_tipo = hectarias * 30

if hectarias > 1000:
    total = hectarias_tipo * 0.95   
elif hectarias_tipo > 3000:
    total = hectarias_tipo * 0.90   
else:
    total = hectarias_tipo

print(f'{nombre}, el valor que tendrá el servicio es de: {total}')


















