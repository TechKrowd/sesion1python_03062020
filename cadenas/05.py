"""
Pedir una cadena por teclado y comprobar si es palíndromo.
"""

cadena = input("Introduce una cadena: ")

aux = cadena.replace(' ','')
aux = aux.replace('\t','')

print(aux)
print("Palíndromo: {}".format(aux == aux[::-1]))