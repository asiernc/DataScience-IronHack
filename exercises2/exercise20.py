precio = input("Introduce un precio con dos decimales (32,24): ")
# Aplicamos un split sep = ','
euros, centimos = precio.split(',')
print(f"""
    Euros: {euros}
    Céntimos: {centimos}
    """)

# version FOR
precio = input("Introduce un precio con dos decimales (32,24): ")
euros = ""
centimos = ""
found_coma = False
for c in precio:
    if c == ",":
        found_coma = True
        continue
    if not found_coma:
        euros += c
    else:
        centimos += c
print(f"""
    Euros: {euros}
    Céntimos: {centimos}
    """)

# version While
precio = input("Introduce un precio con dos decimales (32,24): ")
euros = ""
centimos = ""
i = 0
while i < len(precio) and precio[i] != ",":
    euros += precio[i]
    i += 1
i += 1  # Saltar la coma
while i < len(precio):
    centimos += precio[i]
    i += 1
print(f"""
    Euros: {euros}
    Céntimos: {centimos}
    """)