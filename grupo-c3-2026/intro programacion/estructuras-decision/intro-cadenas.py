# Cadenas (Strings)

# Cadenas multilineas

str="\n" + "El mejor grupo de la tarde es: " + "\n" + "Grupo c3" + "\n"
print(str)
multi = """El mejor grupo de la tarde es:
Grupo C3
"""

print(multi )

menu = """*** MENU ***
1. Guardar producto
2. Buscar producto
3. Editar producto
4. Eliminar producto
5. Reportes de productos

-> Opción {1 a 5}?
"""
print(menu)

# Indexacion de cadenas
# las cadenas se indexan desde cero 

print(multi[0])
print(multi[10])

# longitud de una cadena

print("longitud de una cadena multi",len(multi))

# recorre una cadena 

for i in range (0, len (multi)):
    print(multi[i], end=", ")

for letra in multi:
    print(letra, end=(" * "))

hora1="16:02"
hora2="16:02" 
if ":" in  hora1:
    print("hora1 válida")
else:
    print("hora1 inválida)")
if ":" in hora2:
    print("valida")
else:
    print("inválida")

# INDICES NEGATIVOS

nombre="Luis Santiago"
print(nombre[0])
print(nombre[-1])
print(nombre[-8])

# SLICE

print(nombre[1:5])
print(nombre[3:9])
print(nombre[3:])
print(nombre[3:8:2])
print(nombre[8:3:-1])

# EJEMPLO
"""
Indicar si el texto ingresado por el usuario
es un palindrome.
un palindrome se lee igual en ambas direccioens
"""

texto=input("texto?: ")
if texto == texto[::-1]:
    print("Es un palindrome")
else:
    print("No es un palindrome")
