print("Segundo exercicio")
nota1 = int(input("Escreva a primeira nota: "))
nota2 = int(input("Escreva a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com Distincao")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
