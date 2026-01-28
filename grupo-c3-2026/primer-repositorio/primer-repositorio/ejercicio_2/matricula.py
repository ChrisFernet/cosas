nombre=input("Ingrese el nombre del estudiante: ")
def menu1():
    print("""------------ Menu de Matrícula ----------

------- PROGRAMA FORMATIVO -------
1. Técnico en sistemas
2. Técnico en desarrollo de videojuegos
3. Técnico en animación digital
------- INDICADOR BECA -----------
4. Beca por rendimiento académico 50%.
5. Beca Cultural - Deportes. 40%.
6. No aplica. 
------------------------------
Seleccione una opción...""")


def leer_opcion():
    menu1()
    op=int(input())

    if op < 1  or op > 6:
        print("Opción inválida")
        return None 
    else:
        return op

def matricula(op):
    if op ==1:
        return 800_000
    elif op==2:
        return 1_000_000
    elif op==3:
        return 1_200_000
    else:
        return 0


def descuento(valor_matricula,op):
    dcto = 0

    if op == 4:
        dcto=(valor_matricula*0.5)
    elif op == 5:
        dcto=(valor_matricula*0.4)
    elif op == 6:
        dcto=0
    return dcto


def valor():
    print("Seleccione el programa académico")
    op_programa = leer_opcion()

    if op_programa is None or op_programa < 1 or op_programa > 3:
        print("Programa inválido")
        return 0

    print("Seleccione el tipo de beca")
    op_beca = leer_opcion()

    if op_beca is None or op_beca < 4 or op_beca > 6:
        print("Beca inválida")
        return 0

    valor_matricula = matricula(op_programa)
    descuento_matricula = descuento(valor_matricula, op_beca)

    return valor_matricula - descuento_matricula


total_pagar = valor()

print("Nombre del estudiante:", nombre)
print("Valor final de la matrícula: $", total_pagar)