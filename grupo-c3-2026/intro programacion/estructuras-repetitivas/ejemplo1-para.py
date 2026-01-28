# Estructuras repetitivas - FOR

# Sintaxis 
"""
    for variable in range(rango)
        instruccion1
        instruccion2
        instruccion3

"""
# Range( inicio-fin-salto)
# genera una lista de # desde ini hasta fin-1 que se incrementa
# segun el salto .}

#caso 1
print(list(range(10)))
#caso 2
print(list(range(17,35))) # 1-34
print(list(range(1,11))) # 1-10
#caso 3
print(list(range(0,20,2))) # 0, 2, 4, ...18

#for
#numeros pares hasta 100

for numero in range(0,101, 2):
    print(numero, end=(" - "))

# EJEMPLOS 2
# numeros en un rango indicado por el usuario
ini=int(input("Rango inicial: "))
fin=int(input("Rango final: "))

# if ini 2 != 0 # es impar
#     ini +=1 # ini = ini+1

# for pares in range(ini, fin+1, 2):
#     print(pares, end=", ")

# ejmp 3
# programa que imprima los primeros 7 multiplos de 3

for n in range(7):# range 0,6
    print((n+1)*3,end=", ")