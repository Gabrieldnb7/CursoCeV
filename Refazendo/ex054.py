from datetime import date
maiores = menores = 0
for contador in range (1,8):
    nascimento = int(input('Digite o ano do seu aniversário: '))
    if date.today().year - nascimento >= 18:
        maiores += 1
    else:
        menores += 1
print(f'No total {maiores} pessoas atingiram a maioridade e {menores} são menores de idade.')