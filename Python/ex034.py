s = float(input('Digite o valor do seu salário: '))
if s > 1250.00:
    print('Você receberá um aumento de 10% e seu novo salário será R${:.2f}'.format(s*1.10))
else:
    print('Você receberá um aumento de 15% e seu novo salário será R${:.2f}'.format(s*1.15))
print('Parabéns')
