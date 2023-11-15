print("Por Guilherme ;) 1 Exercicio!")
while True:
    letra = input("Digite uma letra ou 'sair' para encerrar: ")

    if letra == 'sair':
        print("Bye bye!")
        break 
    
    if letra in 'aeiou':
        print("A letra inserida e uma vogal.")
    else:
        print("A letra inserida e uma consoante.")
