# Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = list()
while True:
    valores.append(int(input('Digite um número: ')))
    for valor in valores:
        if valores.count(valor) == 2:
            valores.remove(valor)
            print('Valor duplicado! Retirando da lista.')

# O problema desse meu código é que o valor será adicionado de qualquer forma, só será removido o que for duplicado

    resposta = ' '
    while resposta not in 'NS':
        resposta = (str(input('Quer continuar?[S/N] '))).strip().upper()[0]
    if resposta == 'N':
        break
valores.sort()
print(f'A sua lista é {valores}')
