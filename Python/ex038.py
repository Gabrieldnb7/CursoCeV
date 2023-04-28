n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
if n1 > n2:
    print('\033[31mO primeiro valor é maior do que o segundo.\033[m')
elif n2 > n1:
    print('\033[36mO segundo valor é maior do que o primeiro.\033[m')
elif n1 == n2:
    print('\033[32mOs dois valores são iguais.\033[m')
