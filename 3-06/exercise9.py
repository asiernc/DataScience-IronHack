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
		years = int(input("Introduce los años de estancamiento: "))
		break
	except ValueError:
		print("Por favor, introduce un número válido.")

# B = C * r * t ==> capitalObtneido = capitalInicial * tasa de interes (decimal) * tiempo en años
#capitalObtenido = n * (interes / 100) * years
capitalTotal = n

for i in range(years):
    capitalTotal += capitalTotal * (interes / 100)

ganancia = capitalTotal - n

print(f"El capital obtenido en {years} años, es de {ganancia:.2f} teniendo un acumulado de {capitalTotal:.2f}")
