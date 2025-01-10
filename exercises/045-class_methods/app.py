# Your code here
# Definición de la clase MathOperations
class MathOperations:
    # Variable de clase para el valor de pi
    pi = 3.14159

    @classmethod
    def calculate_circle_area(cls, radius):
        """
        Método de clase para calcular el área de un círculo.
        """
        return cls.pi * radius ** 2

# Usar el método de clase para calcular el área de un círculo con radio 5
circle_area = MathOperations.calculate_circle_area(5)

print(f"Circle Area: {circle_area}")



