# Faça um programa que tenha uma função chamada "área()", que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno
def área(a,b):
    tamanho = (a*b)
    print(f'A área de um terreno de {a:.1f}m * {b:.1f}m é de {tamanho:.1f}m²')


print(f'{"Medidor de Área":^30}')
print('=' * 30)
largura = float(input('Largura (Metros): '))
comprimento = float(input('Comprimento (Metros): '))
área(largura, comprimento)
