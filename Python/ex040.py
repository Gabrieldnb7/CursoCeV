print('\033[1;36mAvaliação de Notas do Semestre\033[m')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
média = (nota1 + nota2) / 2
if média < 5:
    print('Você está \033[31mREPROVADO\033[m!')
elif 5 <= média <= 6.9:
    print('Você está de \033[33mRECUPERAÇÃO\033[m!')
elif média >= 7:
    print('Você está \033[36mAPROVADO\033[m!')
