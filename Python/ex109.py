# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o
# valor retornado por elas vai ou não ser formatado pela função moeda(), desenvolvida no desafio 108
from CursoEmVideo.Módulos import moeda

núm = int(input('Digite um valor: '))
print(f'O valor {moeda.moeda(núm)} aumentado em 80% é {moeda.aumentar(núm, 80, form=True)}')
print(f'O valor {moeda.moeda(núm)} diminuído em 35% é {moeda.diminuir(núm, 35, form=True)}')
print(f'O dobro de {moeda.moeda(núm)} é {moeda.dobro(núm, form=True)}')
print(f'A metade de {moeda.moeda(núm)} é {moeda.metade(núm, form=True)}')
