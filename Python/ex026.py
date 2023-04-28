f = str(input('Digite uma frase: ').strip().lower())
print('Está frase possui {} letras "a"'.format(f.count('a')))
print('A letra "a" aparece primeiro na posição {}'.format(f.find('a')+1))
print('A letra "a" aparece por último na posição {}'.format(f.rfind('a')+1))
