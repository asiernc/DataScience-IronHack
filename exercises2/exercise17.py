str = input("Introduce una frase: ")
# Aplicamos un step negativo para que en vez de hacer izq-der haga der-izq
revStr = str[::-1]
# Mostramos por pantalla
print(revStr)
# Mostramos por pantalla tipo
print(type(revStr))