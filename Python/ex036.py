print('\033[1;32mEmpréstimo bancário para Financeamentos\033[m')
casa = float(input('Digite o valor do imóvel: '))
salário = float(input('Digite o valor de seu salário: '))
anos = int(input('Quantos anos você pretende pagar: '))
## calculando
prestação = casa / (anos * 12)
print('O imovél no valor de R${:.2f} pago em {} anos terá como valor de prestação R${:.2f}' .format(casa, anos ,prestação))
if prestação > (salário * 0.3):
    print('Infelizmente, não sera possível o realizar o financiamento. :(')
elif prestação < (salário * 0.3):
    print('Seu financiamento foi aprovado! O valor mensal será de RS{:.2f} pago em {} meses'.format(prestação,
                                                                                                    (anos * 12)))
print('\033[1;32mFim do processo de financiamento!\033[m')