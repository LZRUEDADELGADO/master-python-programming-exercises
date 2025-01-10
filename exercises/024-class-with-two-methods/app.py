# Your code here
class InputOutString:
    def __init__(self):
        self.input_string = ""

    
    def get_string(self):
        self.input_string = input("Introduce un string: ")

    
    def print_string(self):
        print(self.input_string.upper())

instance = InputOutString()

instance.get_string()      
instance.print_string()   
