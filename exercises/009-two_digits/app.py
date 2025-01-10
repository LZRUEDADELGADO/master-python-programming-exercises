def two_digits(number):
    
    tens = number // 10
    
    units = number % 10
    
    return tens, units


print(two_digits(79)) 
