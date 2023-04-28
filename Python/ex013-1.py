p = float(input('Digite o valor do produto: R$'))
print('O valor do produto é {:.2f} e tem 15% de desconto a vista e um aumento de 10% a prazo'.format(p))
print('O valor do produto a vista é de R${:.2f} com 15% de desconto'.format(p*0.85))
print('O valor do produto a prazo é de R${:.2f} com 10% de aumento'.format(p*1.10))
