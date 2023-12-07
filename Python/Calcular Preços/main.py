def calcular_valor_final(quantidade, preco_unitario, cliente=False):
    valor_sem_desconto = quantidade * preco_unitario
    
    if 3 <= quantidade <= 9:
        desconto_quantidade = 0.07
    elif 10 <= quantidade <= 14:
        desconto_quantidade = 0.1
    elif quantidade >= 15:
        desconto_quantidade = 0.2
    else:
        desconto_quantidade = 0
    
    valor_com_desconto_quantidade = valor_sem_desconto * (1 - desconto_quantidade)
    
    desconto_cliente = 0.03 if cliente else 0
    valor_final = valor_com_desconto_quantidade * (1 - desconto_cliente)
    
    print("Valor sem desconto:", valor_sem_desconto)
    print("Desconto de quantidade:", valor_sem_desconto - valor_com_desconto_quantidade)
    print("Desconto de cliente:", valor_com_desconto_quantidade - valor_final)
    print("Total a pagar:", valor_final)

quantidade = int(input("Escreva a quantidade de produtos: "))
preco_unitario = float(input("Escreva o preço unitário do produto: "))
cliente = input("Você é cliente? (S/N): ").upper() == "S"

calcular_valor_final(quantidade, preco_unitario, cliente)
