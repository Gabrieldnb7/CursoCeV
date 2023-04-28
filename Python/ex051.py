# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.
t1 = float(input('Digite o valor do primeiro termo:'))
r = float(input('Digite o valor da razão:'))
t10 = t1 + (10 - 1) * r
for t in range(1, 11):
    pa = t1 + (t - 1) * r
    print('{:.0f}'.format(pa), end=' -> ')
print('Fim')