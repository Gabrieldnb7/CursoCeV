parênteses = []
expressão = str(input('Digite a expressão: '))
for símbolos in expressão:
    if símbolos == '(' or símbolos == ')':
        parênteses.append(símbolos)
if len(parênteses) % 2 == 0:
    print('A expressão é válida.')
elif len(parênteses) % 2 == 1:
    print('A expressão é inválida.')
print(parênteses)
