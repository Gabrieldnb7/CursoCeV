peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura*altura)
if imc < 18.5:
    print(f'Seu IMC é {imc:.1f} e você está abaixo do peso.')
elif 18.5 <= imc <= 25:
    print(f'Seu IMC é {imc:.1f} e você está no peso ideal.')
elif 25 < imc < 30:
    print(f'Seu IMC é {imc:.1f} e você está com sobrepeso.')
elif 30 < imc < 40:
    print(f'Seu IMC é {imc:.1f} e você está na faixa da obesidade.')
elif imc >= 40:
    print(f'Seu IMC é {imc:.1f} e você está na faixa da obesidade morbida.')
