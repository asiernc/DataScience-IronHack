while True:
	try:
		n = float(input("Introduce una cantidad a invertir: "))
		break
	except ValueError:
		print("Por favor, introduce un número válido.")

while True:
	try:
		interes = float(input("Introduce el intéres anual: "))
		break
	except ValueError:
		print("Por favor, introduce un número válido.")

while True:
	try:
		years = float(input("Introduce los años de estancamiento: "))
		break
	except ValueError:
		print("Por favor, introduce un número válido.")

# B = C * r * t ==> capitalObtneido = capitalInicial * tasa de interes (decimal) * tiempo en años
capitalObtenido = n * (interes / 100) * years

print(f"El capital obtenido en {years} años, es de {capitalObtenido:.2f} teniendo un acumulado de {capitalObtenido + n}")
