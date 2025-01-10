# Your code here
# Clase que genera números divisibles por 7
class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    # Método para encontrar números divisibles por 7
    def generator(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i

# Prueba 
divisible = DivisibleBySeven(50)  # Crear una instancia con n = 50
for num in divisible.generator():  
    print(num, end=" ") 

