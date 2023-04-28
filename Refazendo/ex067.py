print(f'{"Tabuada":=^40}')
while True:
    contador = 1
    núm = int(input('Tabuada de qual valor?[Número negativo interrompe]: '))
    if núm < 0:
        break
    print('=' * 25)
    while contador <= 10:
        print(f'{núm} x {contador:^2} = {núm*contador}')
        contador += 1
    print('=' * 25)

print('Programa encerrado.')
