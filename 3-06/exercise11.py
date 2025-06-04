while True:
	try:
		inicial = float(input("Introduce una cantidad inicial a invertir: "))
		break
	except ValueError:
		print("Por favor, introduce un número válido.")

print("Sabiendo que tienes un 4% de interés anual....")

for i in range(3):
	dif = inicial * 0.04
	print(f"Obteniendo {dif:.2f} anuales.")
	inicial += dif
	print(f"Tu capital asciende a {inicial:.2f} el {i + 1}º año.")