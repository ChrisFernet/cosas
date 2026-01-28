""""
Dar auxilio de transporte a las personas que
ganan menos de dos salarios minimos
"""

# ENTRY Se ingresa el salario 
salario=int(input("Ingrese el salario del trabajador: "))
                
# PROCESS

"""
Sal_minimo=1.700.000
aux_transporte = 0
leer salario
si salario < sal-minimo * 2 entonces
aux_transporte = 300.000
"""

SAL_MINIMO=1_700_000
aux_transporte=0
if salario < (SAL_MINIMO * 2):
    aux_transporte = 300_000
    print("El auxilio de transporte es: ")
else:
    print("No tiene auxilio de transporte")
    aux_transporte=0

# output Se muestra el valor del auxilio de transporte
