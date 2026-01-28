"""
hacer un programa que ayude a los docentes en sus actividades
este programa debe mostrar el siguiente menu 

1 calcular promedio
2 calcular nota mas alta
3 calcular nota mas baja
4 salir

las notas van de 10 a 50
valide que la entrada de las notas sean válidas

el docente podra ingresar cualquier cantidad de notas, cuando
ya no tenga mas notas ingresara 0.

"""

def menu():
    print("""--- TEACHER HELPER ---
1. CALCULAR PROMEDIO
2. NOTA MAS ALTA
3. NOTA MAS BAJA
4. SALIR
------------------------
Seleccione (1-4)         """)
    
def leer_opcion():
    menu()
    op=input()
    while(not op.isdigit() or int(op)<1 or int(op)>4):
        print("Opción no válida, digite un número del 1 al 4: ")
        input("Presione cualquier tecla para continuar...")
        print("\n\n")
        menu()
        op = input()
    return int(op)

def leer_nota(msg):
    while True: 
        try:
            nota = int(input(msg))

            if nota == 0:
                return 0

            if 9 <= nota <= 51:
                return nota
            else:
                print("Error. La nota debe estar entre 10 y 50 (o 0 para terminar).")
                input("Presione Enter para intentar nuevamente...")
        
        except ValueError:
            print("Error. Por favor, ingrese un número válido.")
    

def promedio():
        print("------ PROMEDIO DE NOTAS ------\n")
        nota=leer_nota("Ingrese las notas: ")
        cont=0
        suma=0
        while nota != 0:
             cont+=1
             suma+=nota
             nota=leer_nota("Ingrese una nota: ")
    
        prom=suma/cont
        print(prom)
        return prom
    
def notamax():
    print("------ NOTA MAYOR ------")
    nota=leer_nota("Ingrese las notas: ")
    mayor=0
    while nota !=0:
        nota= leer_nota("Ingrese las notas: ")
        if nota>mayor:
            mayor=nota
    print("La nota mayor es :",mayor)

def notamin():
    print("------ NOTA MENOR ------")
    nota=leer_nota("Ingrese las notas: ") 
    menor=0
    while nota !=0:
        if nota<menor and menor!=0:
            menor=nota
        nota= leer_nota("Ingrese las notas: ")
    print("nota menor:",nota)

def main():
    opcion=0
    while (opcion!=4):
        opcion=leer_opcion()
        if opcion ==1:
            promedio()
        elif opcion ==2:
            notamax()
        elif opcion ==3:
            notamin()
        elif opcion ==4:
            print("\nGracias por usar la calculadora. adios...")
            
        input("Presion1e cualquier tecla para continuar....")
        print("\n\n")
main()
                
     