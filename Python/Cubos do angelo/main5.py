def quadrado_magico(matriz):
    soma = sum(matriz[0])
    for linha in matriz:
        if sum(linha) != soma:
            return False

    for coluna in zip(*matriz):
        if sum(coluna) != soma:
            return False

    if sum(matriz[i][i] for i in range(len(matriz))) != soma:
        return False

    if sum(matriz[i][len(matriz) - 1 - i] for i in range(len(matriz))) != soma:
        return False

    return True

def mostra_quadrados_magicos():
    print("Escreva os números de 1 a 9, separados por espaços:")
    print("Exemplo: 8 3 4 1 5 9 6 7 2")
    entrada = input().split()

    try:
        numeros = [int(num) for num in entrada]
    except ValueError:
        print("Por favor, insira apenas números válidos.")
        return

    if len(numeros) != 9 or set(numeros) != set(range(1, 10)):
        print("Por favor, insira exatamente os números de 1 a 9, sem repetições.")
        return

    matriz = [numeros[i:i+3] for i in range(0, len(numeros), 3)]

    if quadrado_magico(matriz):
        print("É um cubo mágico mágico:")
        for linha in matriz:
            print(" ".join(map(str, linha)))
    else:
        print("Não é um cubo mágico.")

mostra_quadrados_magicos()

