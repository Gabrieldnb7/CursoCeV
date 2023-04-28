palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso','Gratis',
            'Estudar','Praticar','Trabalhar','Mercado','programador','futuro')
#vogais = ('a','e','i','o','u')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos ', end='')
    for letra in palavra.lower():
        if letra in 'aeiou':
            print(f'{letra}',end=' ')
