## Refazer o ex035 e acrescentar código que dira se os triangulos são escalenos, equilateros ou isosceles
print('Formula para Formação de Triângulos')
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
if a + b > c and b + c > a and c + a > b:
    print('Esses valores podem formar um triângulo ', end='')
    if a != b and b != c and c != a:
        print('e este triângulo está classificado como ESCALENO.')
    elif a == b or b == c or c == a:
        print('e este triângulo está classificado como ISÓSCELES.')
    elif a == b and b == c and c == a:
        print('e este triângulo está classificado como EQUILÁTERO.')
    ##### Seria possível terminar está condição aninhada apenas com um else: print('blablabla') porque não é necessario terminar a parte final do codigo
else:
    print('Esses valores não podem formar um triângulo')
