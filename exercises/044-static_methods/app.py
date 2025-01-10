# Your code here
# Definición de la clase MathOperations
class MathOperations:
    @staticmethod
    def add_numbers(num1, num2):
        """
        Método estático para sumar dos números.
        """
        return num1 + num2

# Crear una instancia de MathOperations (opcional, no se necesita para usar un método estático)
math_operations_instance = MathOperations()

# Usar el método estático para sumar dos números
sum_of_numbers = MathOperations.add_numbers(10, 15)

print(f"Sum of Numbers: {sum_of_numbers}")

