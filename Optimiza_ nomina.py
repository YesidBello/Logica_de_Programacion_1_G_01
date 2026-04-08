salario_hora = input('Porfavor ingresar cuanto te pagan por hora trabajada')
horas_mes = input('Ingresa cuantas horas trabaste en el mes')
hijos_numero= input('Ingresa cuantos hijos tienes')
subsidio = 1.200


salario_devengado = salario_hora * horas_mes
 
if salario_devengado < 300.000
   if hijos_numero > 6  
      retencion = 0
    else 
      retencion = 6 - hijos_numero / 2
else
    if hijos_numero < 3
     retencion = 3
    else
     retencion = 10 / hijos numero

retencion_total = salario_devengado * (retencion / 100)
subsidio_hijos = subsidio * hijos_numero
salario_final = salario_devengado + subsidio_hijos - retencion_total


print('Tu salario devengado es:' salario_devengado)
print('La retención sera de:'retancion_total)
print('Recibiras este monto por el subsidio de tus hijos'subsidio_hijos)
print('El total que recibiras sera de:'salario_final)


















































