while True:
	try:
		n = int(input("Introduce un numero entero: "))
		break
	except ValueError:
		print("Por favor, introduce un número válido.")

while True:
	try:
		m = int(input("Introduce un numero entero: "))
		break
	except ValueError:
		print("Por favor, introduce un número válido.")

cociente = n // m
resto = n % m

print(f"{n} entre {m} da un cociente de {cociente} y un resto de {resto}")