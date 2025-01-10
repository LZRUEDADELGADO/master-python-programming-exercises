import math

def print_formula(d):
    
    c = 50
    h = 30
 
    q = math.sqrt((2 * c * d) / h)
    
    return round(q)


print(print_formula(100))  
print(print_formula(90)) 
