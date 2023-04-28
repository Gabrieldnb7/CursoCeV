a = float(input('Valor de A: '))
b = float(input('Valor de B: '))
c = float(input('Valor de C: '))
#if b-c < a < b+c and a-c < b < a+c and a-b < c < b+a:
# AULA
if a < b + c and b < c + a and c < b+a:
    print(f'Com esses lados é possível formar um triângulo.')
else:
    print(f'Com esses segmentos não é possível formar um triângulo.')