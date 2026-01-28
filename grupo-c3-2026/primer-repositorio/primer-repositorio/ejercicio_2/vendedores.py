total_ventas = 0
total_comisiones = 0

cedula = int(input("Ingrese la cédula del vendedor (-1 para terminar): "))

while cedula != -1:
    nombre = input("Ingrese el nombre del vendedor: ")
    tipo = int(input("Ingrese el tipo de vendedor (1, 2 o 3): "))
    ventas = float(input("Ingrese el valor de las ventas del mes: "))

    # Determinar el porcentaje de comisión
    if tipo == 1:
        porcentaje = 0.20
    elif tipo == 2:
        porcentaje = 0.15
    elif tipo == 3:
        porcentaje = 0.25
    else:
        porcentaje = 0
        print("Tipo de vendedor no válido")

    # Calcular comisión
    comision = ventas * porcentaje

    # Mostrar comisión del vendedor
    print("La comisión del vendedor", nombre, "es:", comision)

    # Acumular totales
    total_ventas = total_ventas + ventas
    total_comisiones = total_comisiones + comision

    # Pedir la siguiente cédula
    cedula = int(input("\nIngrese la cédula del vendedor (-1 para terminar): "))

# Resultados finales
print("\nTotal de ventas del mes:", total_ventas)
print("Total a pagar por comisiones:", total_comisiones)
