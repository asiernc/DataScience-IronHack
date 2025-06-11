while True:
	try:
		n = int(input("Introduce una numero entero positivo: "))
		if n <= 0:
			print("Por favor, introduce un número válido.")
			continue
		break
	except ValueError:
		print("Por favor, introduce un número válido.")

odds = []
for i in range(n):
    if i % 2 == 1:
        odds.append(str(i))

print(", ".join(odds))
