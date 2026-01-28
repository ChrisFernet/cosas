"""
print en la pantalla un triangulo de n dimensiones
ejemplo
n=1
salida:
*
n=2
salida
**

n=3
salida
*
**
***
"""

n=int(input("Ingrese las dimensiones: "))

for i in range(1, n+1):# 1,2
    for j in range(1, i+1):
        print("*", end="")
    print()