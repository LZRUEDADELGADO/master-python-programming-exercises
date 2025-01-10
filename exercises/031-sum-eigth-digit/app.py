# Your code here
def all_digits_even():

    even_digit_numbers = []
   
    for num in range(1000, 3001):
        
        if all(int(digit) % 2 == 0 for digit in str(num)):
            even_digit_numbers.append(str(num))
    
    print(",".join(even_digit_numbers))


all_digits_even()
