print("Feito por Gui Pereira :)")
melhornota = -1
piornota = 101
soma = 0
total = 0

while True:
    disciplina = input("Digite o nome da disciplina (0 para sair): ")

    if disciplina == "0":
        break

    nota = int(input("Escreva a nota da disciplina: "))
    total += 1
    soma += nota

    if nota > melhornota:
        melhornota = nota
        melhordisciplina = disciplina

    if nota < piornota:
        piornota = nota
        disciplinapiornota = disciplina

if total > 0:
    media = soma / total
    print(f"Média das notas: {media}")
    print(f"Disciplina com melhor nota: {melhordisciplina}, {melhornota}")
    print(f"Disciplina com pior nota: {disciplinapiornota}, {piornota}")
else:
    print("Nenhuma disciplina foi inserida.")