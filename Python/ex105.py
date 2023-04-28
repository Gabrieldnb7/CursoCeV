# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função

def notas(*nota, sit=False):
    """
        -> função para analisar notas e apresentar a situação de vários alunos.
        :param nota: uma ou mais notas de alunos
        :param sit: valor opcional, indicando se apresentará ou não a situação
        :return: dicionário com várias informações sobre a situação dos alunos.
    """
    dicionário = dict()
    #média = 0
    dicionário["Qtd de Notas"] = len(nota)
    dicionário["Maior nota"] = max(nota)
    dicionário["Menor nota"] = min(nota)
    #for números in nota:
        #média += números
    dicionário["Média"] = sum(nota)/len(nota)
    if sit:
        if dicionário["Média"] >= 6:
            dicionário["Situação"] = 'Aprovado'
        elif dicionário["Média"] <= 5.9:
            dicionário["Situação"] = 'Reprovado'
    return dicionário


boletim = notas(5.5, 2.5, 5, 6.5, sit=True)
print(boletim)
help(notas)
