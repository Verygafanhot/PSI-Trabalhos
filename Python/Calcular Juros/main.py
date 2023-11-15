valor_presente = int(input("Digite o valor presente do investimento: "))
taxa_juros = int(input("Digite a taxa de juros anual (em decimal): "))
periodo_anos = int(input("Digite o numero de anos: "))

taxa_mensal = taxa_juros / 12

total_meses = periodo_anos * 12

valor_futuro = valor_presente * (1 + taxa_mensal) ** total_meses

valor_por_mes = valor_futuro / total_meses

print("Detalhes mensais:")
for mes in range(1, periodo_anos * 12 + 1):
    print(f"Mes {mes}: {valor_por_mes}")

print("O valor total no final do contrato e:", valor_futuro)
