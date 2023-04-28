a = float(input('Digite o comprimento de a: '))
b = float(input('Digite o comprimento de b: '))
c = float(input('Digite o comprimento de c: '))
if a + b > c and b + c > a and c + a > b:
    print('Com essas retas é possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')

a = int(input('Digite um número inteiro: '))