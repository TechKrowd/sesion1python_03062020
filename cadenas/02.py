"""
Leer por teclado una cadena y dos caracteres 
y reemplazar el primero por el segundo todas las veces que aparezca
Repetir el ejercicio anterior, pero reemplazando solo 
la primera aparición del carácter.
"""

cadena = input("Introduce una cadena: ")
ch1 = input("Introduce un caracter: ")[0]
ch2 = input("Introduce otro caracter: ")[0]


cadena2 = cadena.replace(ch1, ch2, 1)
print(cadena2)