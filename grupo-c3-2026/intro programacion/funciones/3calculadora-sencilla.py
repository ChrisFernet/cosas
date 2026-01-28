# hacer un programa que despliegue un menu que permita hacer las operaciones sencillas de una 
# calculadora + - * /

def menu():
    print("""*** CALCULADORA SENCILLA ***
1. SUMA
2. RESTA
3. MULTIPLICACIÓN
4. DIVISIÓN
5. SALIR
----------------
Opción?(1-5) """)
    

def leer_opcion():
    menu()
    op=input()
    while(not op.isdigit() or int(op)<1 or int(op)>5):
        print("Opción no válida, digite un número del 1 al 5: ")
        input("Presione cualquier tecla para continuar...")
        print("\n\n")
        menu()
        op = input()

    return int(op)

def leer_float(msg):
    while (True):
        try:
            str_num=float(input(msg))
            return str_num
        except ValueError:
            print("Error. No es un numero float válido.")
            input("intente nuevamente. presione cualquier tecla para continuar")

def suma():
    print("*** 1. Suma ***")

    n1= leer_float("Ingrese el primer numero: ")
    n2= leer_float("Ingrese el segundo numero: ")
    print(f"La suma es {n1+n2}")
    return n1+n2

def resta():
    print("*** 2. resta ***")

    n1= leer_float("Ingrese el primer numero: ")
    n2= leer_float("Ingrese el segundo numero: ")
    print(f"La resta es {n1-n2}")
    return n1 - n2

def multiplicacion():
    print("*** 3. multiplicación ***")

    n1= leer_float("Ingrese el primer numero: ")
    n2= leer_float("Ingrese el segundo numero: ")
    print(f"La multiplicación es {n1*n2}")
    return n1*n2

def division():
    print("*** 3. división ***")

    n1= leer_float("Ingrese el primer numero: ")
    n2= leer_float("Ingrese el segundo numero: ")
    print(f"La multiplicación es {n1/n2}")
    return n1/n2

def main():
    opcion=0
    while ((opcion!=5)):
        opcion=leer_opcion()

        if opcion ==1:
            suma()
        elif opcion ==2:
            resta()
        elif opcion ==3:
            multiplicacion()
        elif opcion ==4:
            division()
        elif opcion ==5:
            print("\nGracias por usar la calculadora. adios...")
            
        input("Presione cualquier tecla para continuar....")
        print("\n\n")

main()

