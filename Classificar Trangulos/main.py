print("Feito por Gui...")
lado1 = int(input("Escreva o primeiro lado do triângulo: "))
lado2 = int(input("Escreva o segundo lado do triângulo: "))
lado3 = int(input("Escreva o terceiro lado do triângulo: "))

if lado1 == lado2 and lado2 == lado3:
    print("Triângulo Equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")
