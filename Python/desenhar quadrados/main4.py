def desenha_retangulo(largura=1, altura=1):
    largura = max(1, min(largura, 20))
    altura = max(1, min(altura, 20))

    for i in range(altura):
        if i == 0 or i == altura - 1:
            print('+' + '-' * (largura - 2) + '+')
        else:
            print('|' + ' ' * (largura - 2) + '|')

largura_usuario = int(input("Escreva a largura do retângulo (entre 1 e 20): "))
altura_usuario = int(input("Escreva a altura do retângulo (entre 1 e 20): "))

desenha_retangulo(largura_usuario, altura_usuario)
