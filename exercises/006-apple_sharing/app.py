def apple_sharing(n, k):
    
    apples_per_student = k // n
   
    apples_left = k % n
   
    return apples_per_student, apples_left


print(apple_sharing(6, 50))
