def hours_minutes(seconds):
    
    hours = seconds // 3600
    
    minutes = (seconds % 3600) // 60

    return hours, minutes


print(hours_minutes(3900))  
print(hours_minutes(60))    
