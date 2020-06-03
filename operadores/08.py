"""
Pedir al usuario dos fracciones (numerador y denominador) 
y calcular la suma, resta, producto y división de las mismas.
"""

from fractions import Fraction

n = int(input("Introduce el numerador de la primera: "))
d = int(input("Introduce el denominador de la primera: "))

f1 = Fraction(n,d)

n = int(input("Introduce el numerador de la segunda: "))
d = int(input("Introduce el denominador de la segunda: "))

f2 = Fraction(n,d)

suma = f1 + f2
resta = f1 - f2
producto = f1 * f2
division = f1 / f2

print("Suma: {}/{}".format(suma.numerator,suma.denominator))
print("Resta: {}".format(resta))
print("Producto: {}".format(producto))
print("División: {}".format(division))