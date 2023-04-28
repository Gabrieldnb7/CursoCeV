from math import radians, cos, sin, tan
a = float(input('Digite o valor do ângulo: '))
ca = cos(radians(a))
sa = sin(radians(a))
ta = tan(radians(a))
print('Este número tem como seno {:.2f}, Cosseno {:.2f} e Tangente {:.2f}'.format(sa, ca, ta))
