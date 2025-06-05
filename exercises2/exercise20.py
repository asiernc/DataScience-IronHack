precio = input("Introduce un precio con dos decimales (32,24): ")
# Aplicamos un split sep = ','
euros, centimos = precio.split(',')
print(f"""
    Euros: {euros}
    Céntimos: {centimos}
    """)