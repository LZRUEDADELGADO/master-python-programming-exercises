# Your code here

def list_and_tuple(*args):
    
    string_list = [str(arg) for arg in args]
    
    string_tuple = tuple(string_list)
    
    return string_list, string_tuple


result = list_and_tuple(34, 67, 55, 33, 12, 98)
print(result[0])  
print(result[1])  
