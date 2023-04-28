def aumentar(número, porcentagem, form=False):
    if format:
        return moeda(número+(número*porcentagem/100))
    else:
        return número + (número*porcentagem/100)


def diminuir(número,porcentagem, form=False):
    if format:
        return moeda(número-(número*porcentagem/100))
    else:
        return número - (número*porcentagem/100)


def dobro(número, form=False):
    if format:
        return moeda(número * 2)
    else:
        return número * 2


def metade(número, form=False):
    if form:
        return moeda(número / 2)
    else:
        return número / 2


def moeda(dinheiro):
    return f'R${dinheiro:.2f}'


def resumo(número, aumento, dedução):
    print('=' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('=' * 40)
    print(f'Preço analisado: {moeda(número):^23}')
    print(f'Dobro do preço : {dobro(número, form=True):^23}')
    print(f'Metade do preço: {metade(número, form=True):^23}')
    print(f'{aumento}% de aumento : {aumentar(número,aumento,form=True):^23}')
    print(f'{dedução}% de redução : {diminuir(número,dedução,form=True):^23}')
    print('=' * 40)
