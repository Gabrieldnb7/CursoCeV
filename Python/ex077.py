# Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.
palavras = ('Gabinete', 'Processador', 'Programador', 'Fibonacci','Jogador','Computador','Usuário','Trabalho','Estudante','Estudo')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra.upper(), end=' ')
