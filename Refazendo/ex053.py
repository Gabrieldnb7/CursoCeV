inverso = ''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() # para retirar os espaços
junto = ''.join(palavras) # para juntar as palavras sem os espaços
for contador in range(len(junto) - 1, -1, -1):  # len(frase)-1 quer dizer que se tiver 20 letras, ela ira do 0 ao 19
    inverso += junto[contador]  # O inverso receberá as letras de acordo com a posição contada de trás pra frente.
'''É possível trocar o laço por uma função de fatiamento de string que seria: inverso = junto[::-1] que pega a frase 
do início ao fim e inverte ela '''
print(f'A frase {junto} lida de trás para frente é {inverso} ',end='')
if junto == inverso:
    print('e é um palíndromo.')
else:
    print('e não é um palíndromo.')