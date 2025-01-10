# Your code here
def squares_dictionary(n):
   
    squares = {i: i * i for i in range(1, n + 1)}
    
    return squares

print(squares_dictionary(8)) 
