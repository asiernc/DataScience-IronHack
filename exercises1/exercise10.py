while True:
	try:
		n = int(input("Introduce una cantidad de payasos: "))
		break
	except ValueError:
		print("Por favor, introduce un número válido.")

while True:
	try:
		m = int(input("Introduce una cantidad de muñecas: "))
		break
	except ValueError:
		print("Por favor, introduce un número válido.")

weight = (n * 0.112) + (m * 0.075)

print(f"El peso del paquete sera de {weight:.3f} kg.")