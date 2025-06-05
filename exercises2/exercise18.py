str, char = input("Introduce una frase: "), input("Introduce un (1) carácter: ")
# Aplicamos el metodo replace, que se encarga de encontrar esas coincidencias y reemplazarlo.
# Por aquella condición que aplicamos.
formatStr = str.replace(char, char.upper())
print(formatStr)