# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), metade(), dobro().
# Faça também um programa que importe esse módulo e use algumas dessas funções
from CursoEmVideo.Módulos import moeda

número = int(input('Digite um valor: R$'))
print(f'O valor {número} aumentado é {moeda.aumentar(número)}')
print(f'O valor {número} dobrado é {moeda.dobro(número)}')
print(f'O valor {número} diminuido é {moeda.diminuir(número)}')
print(f'O valor {número} pela metade é {moeda.metade(número)}')
