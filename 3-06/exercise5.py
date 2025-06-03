while True:
	try:
		hours = float(input("Introduce tus horas mensuales: "))
		if hours <= 0:
			print("Las horas han de tener valor positivo.")
			continue
		break
	except ValueError:
		print("Por favor, introduce un numero válido.")

while True:
	try:
		salary = float(input("Introduce el salario/hora: "))
		if salary <= 0:
			print("El salario ha de tener valor positivo.")
			continue
		break
	except ValueError:
		print("Por favor, introduce un numero válido.")

count = hours * salary

print(f"La paga que te corresponde sube a: {count}€")