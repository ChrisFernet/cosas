"""
Programa que repita 3 veces hola grupo c3
"""

cont=1
while (cont<=3): # mientras que cont no sea menor o igual a 3 se seguira poniendo el mensaje
    print("Hola grupo c3")
    cont +=1


"""
programa que lea el sexo de una persona.
las opciones son en mayuscula o en minuscula M o F
si lap persona digita correctamente imprime nuevamente el 
sexo del usuario, si no indica que se ha cometido un error y vuelve
a preguntar el sexo hasta que sea bien escrito
"""
print("="*50)

# while(True):
#     sexo=input("\nsexo: ")
#     if sexo == "M" or sexo =="m" or \
#         sexo=="F" or sexo== "f": 
#         break
#     print("error, sexo inválido: (M o F)")
#     input("Intente nuevamente. Presione cualquier tecla para continuar...")
# print("el sexo ingresado fue: ", sexo)
     
# sin ciclo infinito:

sexo=input("\nsexo: ")
while(sexo!= "M" and sexo!= "m"and  sexo!="f"  and sexo!="F"):
    print("error, sexo inválido: (M o F)")
    input("Intente nuevamente. Presione cualquier tecla para continuar...")

    sexo=input("\nsexo: ")
print("el sexo ingresado fue: ", sexo)  