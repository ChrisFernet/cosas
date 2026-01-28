#validar si la fecha es correcta

dia=input(str("Ingrese el día: "))
mes=input(str("Ingrese el mes: "))
año=input(str("Ingrese el año: "))

if mes == ("Enero","Marzo","Mayo","Julio","Agosto","Octubre","Diciembre"):
    if int(dia) == range (1,32):
        print("La fecha es correcta")
    else:
        print("La fecha es incorrecta")
elif mes == ("Abril","Junio","Septiembre","Noviembre"):
    if int(dia) == range (1,31):
        print("La fecha es correcta")
    else:
        print("La fecha es incorrecta")
elif mes=="Febrero":
    if int(año)%4==0 and int(dia) == range (1,30):
        print("La fecha es correcta")
    elif int(año)%4!=0 and int(dia) == range (1,29):
        print("La fecha es correcta")
    else:
        print("La fecha es incorrecta")
else:
    print("La fecha es incorrecta")