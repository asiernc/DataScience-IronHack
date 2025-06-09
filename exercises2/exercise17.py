str = input("Introduce una frase: ")
# Aplicamos un step negativo para que en vez de hacer izq-der haga der-izq
revStr = str[::-1]
# Mostramos por pantalla
print(revStr)
# Mostramos por pantalla tipo
print(type(revStr))

revStr_for = ""
for c in str:
    revStr_for = c + revStr_for

revStr_while = ""
i = len(str) - 1
while i >= 0:
    revStr_while += str[i]
    i -= 1
