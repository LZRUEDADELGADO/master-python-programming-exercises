
def letters_and_digits(text):
    
    counts = {"DIGITS": 0, "LETTERS": 0}
    
 
    for char in text:
        if char.isdigit():  # Verifica si es un dígito
            counts["DIGITS"] += 1
        elif char.isalpha():  # Verifica si es una letra
            counts["LETTERS"] += 1
    
   
    return f"LETTERS {counts['LETTERS']} DIGITS {counts['DIGITS']}"


print(letters_and_digits("hello world! 123"))  
