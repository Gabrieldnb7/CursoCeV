# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um
# valor monétario formatado.
from CursoEmVideo.Módulos import moeda

núm = float(input('Digite um valor: '))

print(f'O valor {moeda.moeda(núm)} aumentado em 80% é {moeda.moeda(moeda.aumentar(núm))}')
print(f'O valor {moeda.moeda(núm)} diminuido em 35% é {moeda.moeda(moeda.diminuir(núm))}')
print(f'O dobro de {moeda.moeda(núm)} é {moeda.moeda(moeda.dobro(núm))}')
print(f'A metade de {moeda.moeda(núm)} é {moeda.moeda(moeda.metade(núm))}')
