# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.
t1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
contador = 1
termos = t1
print('Os primeiros 10 termos da Progressão aritmetica são:')
while contador <= 10:
    print('{} -> '.format(termos), end='')
    termos += r
    contador += 1
print('Fim')
