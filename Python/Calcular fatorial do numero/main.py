print("Como sempre, feito pelo Gui :)")
numero = int(input("Escreva um número inteiro positivo: "))

if numero < 0:
    print("O fatorial não está definido para números negativos.")
elif numero == 0:
    print("O fatorial de 0 é 1")
else:
    resultado = 1
    
    for i in range(1, numero + 1):
        resultado *= i

    print(f"O fatorial de {numero} é {resultado}")
