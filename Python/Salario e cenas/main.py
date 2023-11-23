print("Exercicio 8!!!")
def calcular_reajuste(salario):
    if salario <= 780.00:
        aumento = 0.20
    elif 780.00 < salario <= 900.00:
        aumento = 0.15
    elif 900.00 < salario <= 1500.00:
        aumento = 0.10
    else:
        aumento = 0.05

    aumento = salario * aumento
    novo_salario = salario + aumento

    print("Salario antes do reajuste:", salario)
    print("Percentual de aumento aplicado:", aumento * 100)
    print("Valor do aumento:", aumento)
    print("Novo salario apos o aumento:", novo_salario)

salario_atual = int(input("Escreva o salario atual do colaborador: "))

calcular_reajuste(salario_atual)
 