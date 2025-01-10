def digits_sum(num):
    hundreds = num // 100  
    tens = (num // 10) % 10  
    units = num % 10  
  
    return hundreds + tens + units

print(digits_sum(123)) 
