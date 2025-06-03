while True:
	try:
		kg = float(input("Introduce tu peso en kg (Ex: 68.7kg): "))
		if kg <= 0:
			print("Pesas menos que el aire?.")
			continue
		break
	except ValueError:
		print("Por favor, introduce un peso válido.")

while True:
	try:
		height = float(input("Introduce tu altura en metros (Ex: 1.78): "))
		if kg <= 0:
			print("Como has llegado a medir eso?")
			continue
		break
	except ValueError:
		print("Por favor, introduce una altura válida.")

imc = kg / (height **2)

print(f"Tu IMC resultante es: {imc:.2f}")
