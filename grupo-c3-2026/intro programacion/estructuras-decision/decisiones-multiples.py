"""
notas cualitativas a cuantitativas
según lo siguiente:
----------------------
nota      |   nivel
----------------------
4.5 a 5.0 | superior
4.0 a 4.4 | alto
3.5 a 3.9 | medio 
3.0 a 3.4 | regular
2.0 a 2.9 | deficiente
1.0 a 1.9 | bajo
"""

nota = float(input("Ingrese su nota: "))
if nota >= 4.5 and nota <= 5.0:
    print("superior")
elif 4.0 <= nota <= 4.4:
    print("Alto")
elif 3.5 <= nota <= 3.9:
    print("medio")
elif 3.0 <= nota <= 3.4:
    print("regular")
elif 2.0 <= nota <= 2.9:
    print("deficiente")
elif 1.0 <= nota <= 1.9:
    print("bajo")
else:
    print("Nota inválida.")             

