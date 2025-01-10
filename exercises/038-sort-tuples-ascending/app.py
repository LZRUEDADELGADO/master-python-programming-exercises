# Función para ordenar tuplas en orden ascendente
def sort_tuples_ascending(input_list):
    # Convierte cada string en una tupla separando por comas
    tuples_list = [tuple(item.split(',')) for item in input_list]
    # Ordena las tuplas por los criterios: name, age, score
    sorted_tuples = sorted(tuples_list, key=itemgetter(0, 1, 2))
   
    return sorted_tuples


print(sort_tuples_ascending([
    'Tom,19,80', 'John,20,90', 'Jony,17,91', 'Jony,17,93', 'Jason,21,85'
]))

