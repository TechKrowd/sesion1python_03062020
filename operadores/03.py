"""
Pedir por teclado la edad que tendrá el usuario a final de año 
y el año actual. Sin tener en cuenta el mes de nacimiento, 
calcular el año en que nació el usuario.
"""

edad = int(input("Introduce la edad que tendrás cuando termine el año: "))
year = int(input("Introduce el año actual: "))

nacimiento = year - edad

print(f"Naciste en {nacimiento}")