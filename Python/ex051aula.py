t1 = int(input('Digite o valor do primeiro termo: '))
r = int(input('Digite a razão da PA: '))
t10 = t1 + (10-1)*r
for c in range(t1, t10+1, r):
    print('{}'.format(c), end=' ')