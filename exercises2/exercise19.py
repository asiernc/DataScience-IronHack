# correo = input("Introduce tu correo electronico: ")
# # Guardamos el sufijo de la empresa
# sufijo = "@ceu.es"
# # Aplicamos metodo split y recogemos solo la parte del nombre, no el dominio del @
# # y le concatenamos el sufijo.
# parsed = correo.split('@')[0] + sufijo
# print(parsed)

correo = input("Introduce tu correo electronico: ")
sufijo = "@ceu.es"
nombre = ""
for c in correo:
	if c == '@':
		break
	nombre += c
parsed = nombre + sufijo
print(parsed)

correo = input("Introduce tu correo electronico: ")
sufijo = "@ceu.es"
nombre = ""
i = 0
while i < len(correo) and correo[i] != '@':
    nombre += correo[i]
    i += 1
parsed = nombre + sufijo
print(parsed)
