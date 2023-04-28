# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
# a expressão passada está com os parenteses abertos e fechados na ordem correta

expressão = str(input('Digite a expressão: '))
parênteses = []
for símbolos in expressão:
    if símbolos == '(':
        parênteses.append('(')
    elif símbolos == ')':
        parênteses.append(')')
if len(parênteses) % 2 == 0:
    print('Sua expressão é valida.')
elif len(parênteses) % 2 == 1:
    print('Sua expressão é ínvalida.')
