# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre: A) Quantos números foram digitados.
# B) a lista de valores ordenada de forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista
números = list()
while True:
    números.append(int(input('Digite um número: ')))
    resposta = ' '
    while resposta not in 'NS':
        resposta = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
números.sort(reverse=True)
print(f'Você digitou {len(números)} números')
print(f'A lista na ordem decrescente é {números}')
if 5 in números: # // Essa parte é da aula
# if números.count(5) >= 1: // Essa parte eu fiz
    print('O número 5 está presente na lista.')
else:
    print('O número 5 não está presente na lista')