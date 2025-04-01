# Listas dadas
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Opción 1: Usando bucles for anidados (imprime cada multiplicación)
print("Multiplicaciones individuales:")
for num1 in list1:
    for num2 in list2:
        print(f"{num1} x {num2} = {num1 * num2}")

# Opción 2: Almacenando resultados en una matriz (lista de listas)
print("\nMatriz de resultados:")
resultados = []
for num1 in list1:
    fila = []
    for num2 in list2:
        fila.append(num1 * num2)
    resultados.append(fila)
    print(fila)

# Opción 3: Versión compacta con list comprehension
print("\nMatriz de resultados (list comprehension):")
resultados_lc = [[num1 * num2 for num2 in list2] for num1 in list1]
for fila in resultados_lc:
    print(fila)