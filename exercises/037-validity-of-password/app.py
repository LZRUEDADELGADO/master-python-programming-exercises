# Your code here
import re

# Función para verificar la validez de una contraseña
def valid_password(password):
    # Verificar longitud de la contraseña
    if not (6 <= len(password) <= 12):
        return "Invalid password. Please try again"
    # Verificar al menos una letra minúscula
    if not re.search("[a-z]", password):
        return "Invalid password. Please try again"
    # Verificar al menos una letra mayúscula
    if not re.search("[A-Z]", password):
        return "Invalid password. Please try again"
    # Verificar al menos un número
    if not re.search("[0-9]", password):
        return "Invalid password. Please try again"
    # Verificar al menos un carácter especial
    if not re.search("[$#@]", password):
        return "Invalid password. Please try again"
    
    return "Valid password"


print(valid_password("ABd1234@1"))  
print(valid_password("abcd"))      
