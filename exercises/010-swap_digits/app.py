
def swap_digits(num):
    
    tens = num // 10
    units = num % 10
    
    swapped = units * 10 + tens
    
    return swapped


print(swap_digits(79))  
print(swap_digits(30))  
