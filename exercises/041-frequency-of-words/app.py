import string
# En este ejercicio la funcion esta bine pero hay algun error en una palabra
# Función para calcular la frecuencia de palabras en un string
def compute_word_frequency(sentence):
    # Inicializa un diccionario para contar las frecuencias
    word_frequency = {}

    # Divide el string en palabras y limpia la puntuación
    words = sentence.split()
    cleaned_words = [word.strip(string.punctuation) for word in words]

    # Cuenta la frecuencia de cada palabra limpia
    for word in cleaned_words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    # Ordena el diccionario alfabéticamente por las claves
    sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[0])

    # Imprime cada palabra y su frecuencia en el formato esperado
    for word, frequency in sorted_word_frequency:
        print(f"{word}: {frequency}")

compute_word_frequency("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")

