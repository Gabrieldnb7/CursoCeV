print('~'*30)
print(f'{"Sequência de Fibonacci":^30}')
print('~'*30)
num = int(input('Digite quantos termos da sequência de fibonacci vc quer ver: '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}',end='')
contador = 3
while contador <= num:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    contador += 1
print('\nAcabou')
