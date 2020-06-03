"""
Pedir dos datos numéricos reales al usuario y calcular la suma, 
resta, producto y división de los mismos.
"""

n1 = float(input("Introduce un número real:"))
n2 = float(input("Introduce otro número real:"))

suma = n1 + n2
resta = n1 - n2
producto = n1 * n2
division = n1 / n2

print("La suma es {:.2f}".format(suma))
print("La resta es {:.2f}".format(resta))
print("La producto es {:.2f}".format(producto))
print("La división es {:.2f}".format(division))