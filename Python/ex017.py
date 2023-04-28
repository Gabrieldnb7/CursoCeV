from math import pow, sqrt

x = float(input('Digite o valor do cateto oposto: '))
y = float(input('Digite o valor do cateto adjacente: '))
# h = hypot(x, y)
h = pow(x, 2) + pow(y, 2)
print('O valor da hipotenusa é {:.2f}'.format(sqrt(h)))
