fecha = input("Introduce tu fecha de nacimiento DD/MM/AAAA: ")
dia, mes, anyo = fecha.split('/')
print(f"""
    Día: {dia}
    Mes: {mes}
    Año: {anyo}
    """)