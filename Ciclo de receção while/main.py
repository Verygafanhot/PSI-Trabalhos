print("Script por Gui Pereira")
soma = 0 
contador = 0

while True:
    numero = int(input("Insira um número (0 para sair): "))
    if numero == 0:
        break
    soma += numero
    contador += 1

if contador == 0:
    print("Nenhum número inserido.")
else:
    media = soma / contador
    print(f"A média dos números inseridos é: {media}")
