while True:
	try:
		breads = float(input("Introduce la cantidad de barras de pan NO diarias: "))
		break
	except ValueError:
		print("Por favor, introduce un número válido.")

originalPrice = 3.49
discount = 0.60

descuentoEuros = originalPrice * discount
precioDescontado = originalPrice - descuentoEuros
costeTotal = precioDescontado * breads

print(f"""
	Precio habitual = {originalPrice} €
	Descuento por no ser del día: {discount * 100:.0f} % ({descuentoEuros:.2f} € por barra)
	Precio con descuento por barra: {precioDescontado:.2f} €
	Coste final por {breads:.0f} barras = {costeTotal:.2f} €
	""")