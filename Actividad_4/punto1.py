dep1 = float(input("Ventas Departamento 1: "))
dep2 = float(input("Ventas Departamento 2: "))
dep3 = float(input("Ventas Departamento 3: "))
sal = float(input("Salario base: "))

total_ventas = dep1 + dep2 + dep3
Bono = sal * 0.20
minv = total_ventas * 0.33

print(f"\nVentas totales: ${total_ventas}")
print(f"Minimo de Ventas para bono: ${minv}\n")

if dep1 > minv:
    salario_total = sal + Bono
    print("Departamento 1 Recibe Bono")
else:
    salario_total = sal
    print("Departamento 1 NO recibe Bono")

if dep2 > minv:
    salario_total = sal + Bono
    print("Departamento 2 Recibe Bono")
else:
    salario_total = sal
    print("Departamento 2 NO recibe Bono")

if dep3 > minv:
    salario_total = sal + Bono
    print("Departamento 3 Recibe Bono")
else:
    salario_total = sal
    print("Departamento 3 NO recibe Bono")
