print(" ")
print("guzman 1188")
print(" ")
# Inicializar una lista para almacenar las edades
edades = []

# Solicitar al usuario que ingrese 10 edades
for i in range(10):
    edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))
    edades.append(edad)  # Agregar la edad a la lista

tupla_edades = tuple(edades)

# Contar cuántas personas tienen edades superiores a 20
cantidad_superiores_18 = sum(1 for edad in tupla_edades if edad > 18)

# Imprimir el resultado
print(f"\nCantidad de personas con edades superiores a 20: {cantidad_superiores_18}")