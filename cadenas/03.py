""" 
Leer por teclado varias palabras 
separadas por comas y mostrar solo las que estén en las posiciones pares.
"""

entrada = input("Introduce varias palabras separadas por comas: ")

entrada = entrada.replace(', ',',')

palabras = entrada.split(',')

print(palabras)
print(palabras[::2])