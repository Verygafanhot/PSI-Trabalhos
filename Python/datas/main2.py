from datetime import datetime
print("Obrigado google...")
def formatar_data():
    while True:
        data_input = input("Por favor, insira uma data no formato DD-MM-YYYY: ")

        try:
            data_obj = datetime.strptime(data_input, '%d-%m-%Y')
            
            data_formatada = data_obj.strftime('%d/%m/%Y')
            
            return data_formatada
        except ValueError:
            print("Data inválida. Tente novamente.")

data_formatada = formatar_data()

print("A data formatada é:", data_formatada)
