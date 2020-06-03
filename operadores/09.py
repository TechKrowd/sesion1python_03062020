"""
Pedir dos números enteros por teclado. Realizar la división entera del primero 
entre el segundo y 
calcular el resto de dicha división. Mostrar ambos resultados.
"""

n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce otro número: "))

d = n1 // n2
r = n1 % n2

print("División: {}".format(d))
print("Resto: {}".format(r))