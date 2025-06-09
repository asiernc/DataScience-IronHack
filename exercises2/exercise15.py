# # Preguntamos nombre y parseamos a upper
# name = input("Introduce tu nombre: ").upper()
# # contamos letras y guardamos
# len = len(name)
# print(f"{name} tiene {len} letras.")


name, i = input("Introduce tu nombre: ").upper(), 0

while name[:i] != name:
    i += 1

print(f"{name} tiene {i} letras.")