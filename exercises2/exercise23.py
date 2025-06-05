prod = input("Introduce un producto: ")
precio = input("Introduce su precio (32.24): ")
unds = input("Introduce las unidades: ")

if '.' in precio:
    precio_str = precio.split('.')
    precio_str[0] = precio_str[0].zfill(6)
    precio_str[1] = precio_str[1].ljust(2, '0')
    precio_str = '.'.join(precio_str)
else:
    precio_str = precio.zfill(6) + '.00'

unds = unds.zfill(3)

coste = float(precio) * int(unds)
coste_entero, coste_decimal = f"{coste:.2f}".split('.')
coste_entero = coste_entero.zfill(8)
coste_str = f"{coste_entero}.{coste_decimal}"

str = f"{prod.title()}\t{precio_str}\t{unds}\t{coste_str}"
print(str)