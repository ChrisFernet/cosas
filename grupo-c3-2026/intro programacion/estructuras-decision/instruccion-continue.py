# INSTRUCCION CONTINUE
"""
    salta las instrucciones de un ciclo a
    la siguiente iteracion

"""
#liste los numeros impares entre los numeros 1 
#y 100, ignore aquellos numeros que sean 
#multiplos de 3 y 5

for num in range(1,101,2):
    if num %3 == 0 or num %5 == 0:
        continue
    print(num, end=", ") 