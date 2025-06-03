while True:
	try:
		n = float(input("Introduce una cantidad inicial a invertir: "))
		break
	except ValueError:
		print("Por favor, introduce un número válido.")

print("Sabiendo que tienes un 4% de interés anual....")

for i in range(3):
    obt = n * 0.04
    print(f"Obteniendo {obt:.2f} anuales.")
    n += obt
    print(f"Tu capital asciende a {n:.2f} el {i + 1}º año.")