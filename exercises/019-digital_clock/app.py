def digital_clock(n):
    
    hours = (n // 60) % 24  
    minutes = n % 60  
    return hours, minutes

print(digital_clock(150))  
print(digital_clock(1440))  
print(digital_clock(1439))  
