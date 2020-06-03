"""
Leer una cadena por teclado y mostrar por pantalla lo siguiente:
-Los n primeros caracteres. N se solicitará por teclado.
-Los n últimos caracteres. N se solicitará por teclado.
-Los caracteres que ocupan las posiciones pares dentro de la cadena.
-La cadena al revés
"""

cadena = input("Introduce una cadena: ")
n = int(input("Introduce n: "))

print(cadena[:n])
print(cadena[len(cadena)-n:])
print(cadena[::2])
print(cadena[::-1])