# Your code here
# Definición de la clase Book
class Book:
    def __init__(self, title, author, year):
        """
        Inicializa los atributos del libro: título, autor y año.
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """
        Devuelve una representación en forma de cadena del libro.
        """
        return f"Book Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}"

# Creación de una instancia de la clase Book
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

# Prueba del método __str__ al imprimir la instancia
print(book1)



