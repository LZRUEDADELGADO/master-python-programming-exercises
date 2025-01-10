# Your code here

def divisible_binary(input_string):
    
    binary_numbers = input_string.split(",")
    
    divisible_by_5 = [
        binary for binary in binary_numbers if int(binary, 2) % 5 == 0
    ]
    
    return ",".join(divisible_by_5)


print(divisible_binary("0100,0011,1010,1001")) 
