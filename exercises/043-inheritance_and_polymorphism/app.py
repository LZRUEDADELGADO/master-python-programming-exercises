### DON'T modify this code ###

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        return f"Hello! I am {self.name}, I am {self.age} years old, and my current grade is {self.grade}."

    def study(self, hours):
        return f"{self.name} is studying for {hours} hours."
        
### DON'T modify the code above ###
        
### ↓ Your code here ↓ ###

# Clase que hereda de Student
class CollegeStudent(Student):
    def __init__(self, name, age, grade, major):
        # Llama al constructor de la clase padre
        super().__init__(name, age, grade)
        self.major = major

    def introduce(self):
        # Sobrescribe el método introduce
        return f"Hi there! I'm {self.name}, a college student majoring in {self.major}."

    def attend_lecture(self):
        # Nuevo método exclusivo de CollegeStudent
        return f"{self.name} is attending a lecture for {self.major} students."

# Crear una instancia de CollegeStudent
college_student = CollegeStudent("Alice", 20, 90, "Computer Science")

# Llamar a los métodos
print(college_student.introduce())         # Hi there! I'm Alice, a college student majoring in Computer Science.
print(college_student.attend_lecture())   # Alice is attending a lecture for Computer Science students.
print(college_student.study(3))           # Alice is studying for 3 hours.
