# Your code here

def square_odd_numbers(input_string):
    # Divide el string en una lista de números y convierte cada uno a entero
    numbers = map(int, input_string.split(","))
    # Filtra los números impares y eleva cada uno al cuadrado
    squared_odds = [num ** 2 for num in numbers if num % 2 != 0]
    # Retorna la lista de números impares elevados al cuadrado
    return squared_odds


print(square_odd_numbers("1,2,3,4,5,6,7,8,9")) 
