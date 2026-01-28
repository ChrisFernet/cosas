

def menu():
    print("""*** Nequi ***
1. CARGAR SALDO
2. PAGAR
3. Transferir dinero
4. Mostrar saldo
5. Salir
----------------
Opción?(1-5) """)

def leer_opcion():
    op=input()
    while(not op.isdigit() or int(op)<1 or int(op)>5):
        print("Opción no válida, digite un número del 1 al 5: ")
        input("Presione cualquier tecla para continuar...")
        print("\n\n")
        menu()
        op = input()

    return int(op)

def cargar_saldo(saldo):
    monto = int(input("Ponga el monto a ingresar: "))
    if monto < 1:
        print("Monto inválido. presione para continuar.")
        input()
        return saldo
    else:
        print("El nuevo saldo es: ", saldo + monto)
    return saldo + monto

def pagar(saldo):
    monto = int(input("Ponga el monto a pagar: "))
    if monto < 1:
        print("Monto inválido. presione para continuar.")
        input()
        return saldo

    elif monto > saldo:
        print("Saldo insuficiente.")
        input()
        return saldo

    if monto < saldo:
        saldo - monto
        print("Operación exitosa.")
    return saldo - monto

def celular_isnumeric(celular):
    for num in celular:
        if not num.isdigit():
            return False
    return True

def transferir(saldo):
    celular = input("Ingrese su número de celular: ")
    monto = int(input("Ingrese el monto a transferir: "))
    if not (len(celular) == 10 and celular_isnumeric(celular)):
        print("Número inválido.")
        print("\n\n")
        menu()
    elif monto < 1:
        print("Monto inválido. presione para continuar.")
        print("\n\n")
        menu()
        monto = input()
    elif monto > saldo:
        print("Saldo insuficiente.")
        print("\n\n")
        menu()
    elif monto < saldo:
        saldo - monto
        print("Operación exitosa.")

def mostrar_saldo(saldo):
    print("El saldo actual es: ", saldo)
 

def main():
    opcion=0
    ingreso=0
    saldo=0
    while ((opcion!=5)):
        menu()
        opcion=leer_opcion()

        if opcion ==1:
            saldo = cargar_saldo(saldo)
        elif opcion ==2:
            saldo = pagar()
        elif opcion ==3:
            transferir()
        elif opcion ==4:
            mostrar_saldo(saldo)
        elif opcion ==5:
            print("\nGracias por usar la calculadora. adios...")
            
        input("Presione cualquier tecla para continuar....")
        print("\n\n")

main()