def two_timestamp(hr1, min1, sec1, hr2, min2, sec2):
    
    timestamp1 = hr1 * 3600 + min1 * 60 + sec1
    timestamp2 = hr2 * 3600 + min2 * 60 + sec2
    
    return timestamp2 - timestamp1


print(two_timestamp(1, 1, 1, 2, 2, 2))  
print(two_timestamp(1, 2, 30, 1, 3, 20))  