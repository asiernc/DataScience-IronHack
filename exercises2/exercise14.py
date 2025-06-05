name = input("Introduce tu nombre completo: ")
# Hacemos un bucle de 0,1,2
for i in range(3):
    # Si es la primera iteración, parseamos a minus
    if i == 0:
        print(name.lower())
    # Si es la segunda iteración, parseamos a mayus
    elif i == 1:
        print(name.upper())
    # Si es la tercera iteración, parseamos como title (1ª char mayus/palabra)
    else:
        print(name.title())