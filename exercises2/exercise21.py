fecha = input("Introduce tu fecha de nacimiento DD/MM/AAAA: ")
dia, mes, anyo = fecha.split('/')
print(f"""
    Día: {dia}
    Mes: {mes}
    Año: {anyo}
    """)

# Versión usando for
fecha = input("Introduce tu fecha de nacimiento DD/MM/AAAA: ")
dia = ""
mes = ""
anyo = ""
part = 0
for c in fecha:
    if c == "/":
        part += 1
        continue
    if part == 0:
        dia += c
    elif part == 1:
        mes += c
    else:
        anyo += c
print(f"""
    Día: {dia}
    Mes: {mes}
    Año: {anyo}
    """)

# Versión usando while
fecha = input("Introduce tu fecha de nacimiento DD/MM/AAAA: ")
dia = ""
mes = ""
anyo = ""
i = 0
# Día
while i < len(fecha) and fecha[i] != "/":
    dia += fecha[i]
    i += 1
i += 1  # Saltar la barra
# Mes
while i < len(fecha) and fecha[i] != "/":
    mes += fecha[i]
    i += 1
i += 1  # Saltar la barra
# Año
while i < len(fecha):
    anyo += fecha[i]
    i += 1
print(f"""
    Día: {dia}
    Mes: {mes}
    Año: {anyo}
    """)