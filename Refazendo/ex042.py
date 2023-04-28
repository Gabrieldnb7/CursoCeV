a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
if a + b > c and b + c > a and a + c > b:
    print(f'Esses segmentos podem formar um triângulo',end=' ')
    if a == b == c:
        print('e será um triângulo equilátero.')
    elif a == b or b == c or a == c:
        print('e será um triângulo isósceles.')
    elif a != b or b != c or a != c:
        print('e será um triângulo escaleno.')
else:
    print('Esses segmentos não podem formar um triângulo.')
