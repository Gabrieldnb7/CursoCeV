frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''
# o for in range poderá ser substituído por um tratamento de strings do python
# com o codigo inverso = juntar[::-1] que significa que pegará o juntar do início ao fim e o inverterá
# (len(juntar) transforma as palavras em números de acordo com a posição
for letras in range(len(juntar) - 1, -1, -1):  # neste range, len(juntar)-1 porque a numeração começará do 0,
    # -1 seguinte porque o ultimo número a ser considerado deverá ser 0 e o -1 final é para diminuir de 1 em 1.
    inverso += juntar[letras]  # codigo para inverter a frase
print('A frase {} de trás para frente é {}'.format(juntar, inverso))
if inverso == juntar:
    print('Está frase é um palíndromo.')
else:
    print('Está frase não é um palíndromo')
