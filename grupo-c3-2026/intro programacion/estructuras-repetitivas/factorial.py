# haga un programa que calcule el factorial de un número 
n=int(input("Ingrese un número: "))
fact= 1

for i in range(1, n+1):
    fact*= i# fact= facto* i
print("El factorial de", n," es ", fact) 

# ejercicio 1
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

