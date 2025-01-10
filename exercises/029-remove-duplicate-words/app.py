# Your code here

def remove_duplicate_words(input_string):
    
    unique_words = set(input_string.split())
    
    sorted_words = sorted(unique_words)
    
    return " ".join(sorted_words)


print(remove_duplicate_words("hello world and practice makes perfect and hello world again"))

