"""
Toma cualquier numero entero positivo 

si el numero es par, dividelo entro 2
si el numero es impar, multiplicalo por 3 y sumale 1
repite este proceso con el resultado que obtengas, una y otra vez

la conjetura dice que, sin importar con que numero empieces, siempre
terminaras llegando al numero 

empieza con 6

6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
"""

import random

num=random.randint(1, 10)
print(num, end=" -> ")
while(num != 1):
    if num %2 == 0:
        num = num //2
    else:
        num= num * 3 + 1
    print(num, end=" -> ")
