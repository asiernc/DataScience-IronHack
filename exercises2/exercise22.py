compra = input("Introduce tu compra separado por ',' (Ex: manzana,huevos,leche): ")
# Aplicamos split por comas
list = compra.split(',')
# Creamos un bucle del len de list y mostramos valor
for i in range(len(list)):
    print(list[i])