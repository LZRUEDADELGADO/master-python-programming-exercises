# Your code here
# Definimos la clase Student
class Student:
    def __init__(self, name, age, grade):
        """
        Método especial para inicializar los atributos de la clase.
        name: Nombre del estudiante
        age: Edad del estudiante
        grade: Nota inicial del estudiante
        """
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        """
        Método para presentar al estudiante.
        """
        return f"Hello! I am {self.name}, I am {self.age} years old, and my current grade is {self.grade}."

    def study(self, hours):
        """
        Método para simular el acto de estudiar.
        Incrementa la nota del estudiante en función de las horas estudiadas.
        """
        self.grade += hours * 0.5
        return f"After studying for {hours} hours, {self.name}'s new grade is {self.grade}."


# Creamos una instancia de la clase Student
student1 = Student("Ana", 20, 80)

# Probamos los métodos de la clase
print(student1.introduce())  # Presenta al estudiante
print(student1.study(3))     # Simula que el estudiante estudia durante 3 horas

