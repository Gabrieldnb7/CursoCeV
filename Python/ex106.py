# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra "Fim", o programa se encerrará.
from time import sleep
cores = ('\033[m',           # 0 -> Sem cor
         '\033[0;30;41m',    # 1 -> Vermelho
         '\033[0;30;42m',    # 2 -> Verde
         '\033[0;30;43m',    # 3 -> Amarelo
         '\033[0;30;44m',    # 4 -> Azul
         '\033[0;30;45m',    # 5 -> Roxo
         '\033[0;30;46m'     # 6 -> Ciano
         )


def ajuda(msg):
    título(f'Acessando o manual do comando \'{comando}\'',3)
    sleep(1)
    print(cores[2], end='')
    help(msg)
    print(cores[0], end='')
    sleep(1)


def título(msg, cor=0):
    tamanho = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(cores[0], end='')
    sleep(1)


while True:
    título('Sistema de Ajuda PyHelp', 6)
    sleep(1)
    print(cores[1], end='')
    comando = str(input('Função ou Biblioteca > ')).strip()
    print(cores[0], end='')
    if comando.lower() == 'fim':
        título('Até logo', 4)
        break
    else:
        ajuda(comando)
