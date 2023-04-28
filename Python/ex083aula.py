expressão = str(input('Digite a expressão númerica: '))
parênteses = []
for símbolos in expressão:
    if símbolos == '(':
        parênteses.append('(')
    elif símbolos == ')':
        if len(parênteses) > 0:
            parênteses.pop()
        elif len(parênteses) == 0:
            parênteses.append(')')
if len(parênteses) == 0:
    print('Sua expressão é valida')
elif len(parênteses) >= 1:
    print('Sua expressão é invalida')
# Neste exercício, o professor propoe que, ao analisar a expressão devemos utilizar como parâmetro as duplas de
# parênteses "()" que, quando formadas, serão excluidas da lista. Se ainda restar valores dentro da lista de
# parênteses, quer dizer que o usuário colocou parênteses a mais na expressão e ela está incorreta.
