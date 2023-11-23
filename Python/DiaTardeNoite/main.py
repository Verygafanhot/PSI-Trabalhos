
print("Exercicio 7")
def obter_turno():
    turno = input("Escreva M para Matutino, V para Vespertino ou N para Noturno: ")
    return turno.upper() 

def saudacao(turno):
    if turno == "M":
        print("Bom Dia!")
    elif turno == "V":
        print("Boa Tarde!")
    elif turno == "N":
        print("Boa Noite!")
    else:
        print("Valor Invalido!")

turno_usuario = obter_turno()
saudacao(turno_usuario)
