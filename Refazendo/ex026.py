frase = str(input('Digite um frase: ')).strip().lower()
print(f'A letra "a" aparece {frase.count("a")} vezes')
print(f'A letra "a" aparece pela primeira vez na posição {frase.find("a")+1}')
print(f'A letra "a" aparece pela última vez na posição {frase.rfind("a")+1}')