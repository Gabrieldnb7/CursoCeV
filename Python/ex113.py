# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
# de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            núm = int(input('Digite um valor inteiro: '))
        except (ValueError, TypeError):
            print('\033[31mErro! por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('O usuário preferiu não informar o valor inteiro.')
            return 0
        else:
            return núm


def leiaFloat(msg):
    while True:
        try:
            núm = float(input('Digite um valor real: '))
        except (ValueError, TypeError):
            print('\033[31mErro! por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\nO usuário preferiu não informar o valor real.')
            return 0
        else:
            return núm


inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {inteiro} e o número real {real}')
