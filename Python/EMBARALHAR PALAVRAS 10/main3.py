import random

def embaralhar_string(input_string):
    input_string = input_string.lower()

    caracteres_embaralhados = random.sample(input_string, len(input_string))

    string_embaralhada = ''.join(caracteres_embaralhados)

    return string_embaralhada
palavra_original = input("Escreva a palavra: ")

palavra_embaralhada = embaralhar_string(palavra_original)

print("Palavra embaralhada:", palavra_embaralhada)
