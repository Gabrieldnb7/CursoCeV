# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as
# funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo funcionando.
from ex111.utilidadesCeV import moeda
núm = int(input('Digite um valor: '))
moeda.resumo(núm, 35, 22)
