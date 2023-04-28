soma = contador = 0
while True:
    número = int(input('Digite um número[Digite 999 para terminar]: '))
    if número == 999:
        break
    soma += número
    contador += 1
print(f'Você digitou {contador} números e a soma deles é {soma}')