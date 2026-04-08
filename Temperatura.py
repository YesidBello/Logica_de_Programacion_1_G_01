temperaturas = []
dia = 0
while dia < 30:
    temp = float(input(f"Día {dia+1}: "))
# lo que hace el float es poder tener datos decimales, en imput hace que aparezca que se busca un dato y lo ultimo busca un dato cada dia.
    temperaturas.append(temp)
# Lo que hace es que los datos se metan a una lista llamada temp
    dia += 1
promedio = sum(temperaturas) / 30
dias_mayor = sum(1 for t in temperaturas if t > promedio)
# 1 for t in temperaturas lo que hace es leer todas las temperaturas, t > promedio lo que hace es ver cuales son mayores, sum cuantos dias cumplen esto
dias_menor = sum(1 for t in temperaturas if t < promedio)

temp_max = max(temperaturas)
temp_min = min(temperaturas)

print ('Los resultados fueron:')
print (f'1. El promedio de temperatura registrado estos 30 dias fue: {promedio}')
print (f'2. Estos fueron el total de dias que hizo más temperatura que el promedio: {dias_mayor}')
print (f'3. Estos fueron el total de dias que hizo menos temperatura que el promedio: {dias_menor}')
print (f'4. Esta fua la temperatura mayor que hubo durante el mes: {temp_max}')
print (f'5. Esta fua la temperatura menor que hubo durante el mes: {temp_min}')


