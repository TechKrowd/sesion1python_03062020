"""
Pedir por teclado el precio base de un producto y calcular 
el iva y el precio final del mismo.
"""

precio_base = float(input("Introduce el precio base"))
precio_final = precio_base * 1.21
iva = precio_final - precio_base

print("El precio final es {:.2f} y el iva es {:.2f}".format(precio_final, iva))