"""
Pedir un número entero por teclado y calcular su cuadrado.
"""

n = int(input("Introduce un número: "))
#cuadrado = n ** 2
cuadrado = pow(n,2)

print("El cuadrado de {} es {}".format(n,cuadrado))