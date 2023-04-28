produto = float(input('Digite o valor do produto: R$'))
pagamento = int(input('Digite a forma de pagamento:\n[ 1 ] à vista no pix.\n[ 2 ] à vista no cartão.\n[ 3 ] para 2x '
                      'no cartão.\n[ 4 ] para 3x ou mais no cartão.\n'))
if pagamento == 1:
    print(f'O produto terá 10% de desconto e ficará R${produto-(produto*0.10):.2f}')
elif pagamento == 2:
    print(f'O produto terá 5% de desconto e ficará R${produto-(produto*0.05):.2f}')
elif pagamento == 3:
    parcela = produto / 2
    print(f'O valor da parcela do produto em 2x será de R${parcela:.2f}')
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'O produto no valor de {produto:.2f} parcelado em {parcelas:.2f} vezes ficará {produto+(produto*0.2):.2f}')
else:
    print('Opção inválida, tente novamente!')
