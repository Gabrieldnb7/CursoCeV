# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e o outro chamado show que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.
def fatorial(num, show=False):
    """fatorial(num, show=False
            -> Calcula o valor fatorial de um número
            :param num: O número a ser fatorado
            :param show: (opcional) mostra ou não a conta
            :return: O valor do fatorial de um número."""
    fat = 1
    for contador in range(num, 0, -1):
        fat *= contador
        if show:
            print(contador, end='')
            if contador > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

    return fat


#n1 = int(input('Digite um número: '))
print(fatorial(5, show=True))