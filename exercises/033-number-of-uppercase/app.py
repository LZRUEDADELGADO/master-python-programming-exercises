# Your code here

def number_of_uppercase(text):
    
    counts = {"UPPERCASE": 0, "LOWERCASE": 0}
    
    for char in text:
        if char.isupper():  # Verifica si el carácter está en mayúscula
            counts["UPPERCASE"] += 1
        elif char.islower():  # Verifica si el carácter está en minúscula
            counts["LOWERCASE"] += 1
    
    return f"UPPERCASE {counts['UPPERCASE']} LOWERCASE {counts['LOWERCASE']}"


print(number_of_uppercase("Hello world!"))  
