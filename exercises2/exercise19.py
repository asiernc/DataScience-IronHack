correo = input("Introduce tu correo electronico: ")
# Guardamos el sufijo de la empresa
sufijo = "@ceu.es"
# Aplicamos metodo split y recogemos solo la parte del nombre, no el dominio del @
# y le concatenamos el sufijo.
parsed = correo.split('@')[0] + sufijo
print(parsed)