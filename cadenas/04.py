"""
Pedir dos cadenas por teclado 
y comprobar si la primera es subcadena de la segunda.
"""

cad1 = input("Introduce la primera cadena: ")
cad2 = input("Introduce la segunda cadena: ")

print("Cadena encontrada: {}".format(cad2.find(cad1)!=-1))