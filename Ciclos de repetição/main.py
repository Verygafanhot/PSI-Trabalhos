print("Por Guilherme Pereira, tentei fazer de uma forma diferente a forma de sair do programa e... funcionou!")
mais_de_2_filhos = 0
menos_ou_2_filhos = 0

num_pessoas = int(input("Quantas pessoas você quer perguntar: "))

pessoa_atual = 0
while pessoa_atual < num_pessoas:
    num_filhos = int(input(f"Quantos filhos a pessoa {pessoa_atual} tem:"))
    
    if num_filhos > 2:
        mais_de_2_filhos += 1
    else:
        menos_ou_2_filhos += 1
    
    pessoa_atual += 1

print(f"Pessoas com mais de 2 filhos: {mais_de_2_filhos}")
print(f"Pessoas com 2 ou menos filhos: {menos_ou_2_filhos}")