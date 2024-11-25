print(" ")
print("guzman guzman 1188")
print(" ")
def max_in_list(numbers):
    if not numbers:
        raise ValueError("La lista no puede estar vacía.") 

    max_number = numbers[0]  # Inicializa el máximo con el primer número de la lista
    for number in numbers[1:]:  # Itera a través de los números restantes
        if number > max_number:  # Si el número actual es mayor que el máximo encontrado
            max_number = number  # Actualiza el máximo
    return max_number  # Devuelve el máximo encontrado

try:
    lista_de_numeros = [5, 7, 1, 6, 2]
    maximo = max_in_list(lista_de_numeros)
    print(f"El número máximo en la lista es: {maximo}")
except ValueError as e:
    print(e)