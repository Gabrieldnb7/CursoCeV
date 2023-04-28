print('\033[1;36mCálculo de IMC\033[m')
peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso/(altura**2)
print('O valor do seu IMC é {:.2f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Você está na faixa da obesidade.')
elif imc >= 40:
    print('Você está na faixa de obesidade morbida.')