edad=int(input("Ingrese su edad: "))

if edad in range(0,13):
    print("Es usted un niño")
elif edad in range(12,18):
    print("Es usted un adolescente")
elif edad in range(17,36):
    print("Es usted un adulto joven")
elif edad in range(35,66):
    print("Es usted un adulto")
elif 66 <= edad:
    print("Es usted un adulto mayor") 
