tlf = input("Introduce tu numero de empresa (+XX-0123456789-XX): ")
# Aplicamos un split para que separe el str original por el caracter '-'
tlfSplit = tlf.split('-')
# Printamos el valor del medio que es el que continene el numero
print(tlfSplit[1])