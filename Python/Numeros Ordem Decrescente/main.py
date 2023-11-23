def ler_numeros():
    num1 = int(input("Escreva o primeiro numero: "))
    num2 = int(input("Escreva o segundo numero: "))
    num3 = int(input("Escreva o terceiro numero: "))
    return num1, num2, num3

def ordem(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort(reverse=True)
    print("Numeros em ordem decrescente:", numeros)

num1, num2, num3 = ler_numeros()
ordem(num1, num2, num3)
