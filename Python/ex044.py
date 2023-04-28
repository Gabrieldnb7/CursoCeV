preço = float(input('Digite o valor das compras: R$'))
condição = int(input('Qual será a condição de pagamento?\n'
                     'Digite 1 para pagamento à vista no dinheiro\n'
                     'Digite 2 para pagamento à vista no cartão\n'
                     'Digite 3 para pagamento em até 2x no cartão\n'
                     'Digite 4 para pagamento em 3x ou mais no cartão\n'))
if condição == 1:
    preço = preço * 0.9
    print('Suas compras terão desconto de 10% e ficarão no valor de  R${:.2f}'.format(preço))
elif condição == 2:
    preço = preço * 0.95
    print('Suas compras terão 5% de desconto e ficarão no valor de R${:.2f}'.format(preço))
elif condição == 3:
    print('Não haverá alteração e suas compras ficarão no valor de R${:.2f}'.format(preço))
elif condição == 4:
    parcelas = int(input('Quantas parcelas? '))
    preço = preço * 1.2
    total = preço / parcelas
    print('Suas compras de {:.2f} sairão em parcelas de {:.2f} devido aos 20% de juros'.format(preço, total))
else:
    print('Opção inválida, tente novamente.')
