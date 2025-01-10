
def sequence_of_words(input_string):
    
    words = input_string.split(",")
   
    sorted_words = sorted(words)
    
    return ",".join(sorted_words)


print(sequence_of_words("without,hello,bag,world"))
