import random
print("Isto está uma confusão mas se funciona eu não mexo mais")
def jogar_craps():
    print("Bem-vindo!")

    primeira_jogada = lancar_dados()
    print("Você tirou um total de", primeira_jogada)

    if primeira_jogada == 7 or primeira_jogada == 11:
        print("Você ganhou! É um 'natural'.")
    elif primeira_jogada == 2 or primeira_jogada == 3 or primeira_jogada == 12:
        print("Você perdeu! É um 'craps'.")
    else:
        print("Seu ponto é:", primeira_jogada)
        continuar_jogando(primeira_jogada)

def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    total = dado1 + dado2
    return total

def continuar_jogando(ponto):
    while True:
        input("Pressione Enter para lançar os dados novamente...")
        resultado = lancar_dados()
        print("Você tirou um total de", resultado)

        if resultado == ponto:
            print("Você ganhou! Tirou o ponto novamente.")
            break
        elif resultado == 7:
            print("Você perdeu! Tirou um 7 antes de conseguir o ponto novamente.")
            break

if __name__ == "__main__":
    jogar_craps()
