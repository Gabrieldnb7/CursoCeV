salário = float(input('Digite o valor do seu salário: R$'))
casa = float(input('Digite o valor do imóvel: R$'))
anos = int(input('Em quantos anos você ira parcelar? '))
prestação = casa / (anos*12)
print(f'Para pagar um imóvel no valor de R${casa:.2f} em {anos} anos a prestação será de R${prestação:.2f}')
if prestação > salário*0.3:
    print(f'Infelizmente seu emprestimo foi negado.')
else:
    print(f'Seu emprestimo foi aprovado!') #O valor da prestação será de {prestação:.2f} paga em {anos} prestações')