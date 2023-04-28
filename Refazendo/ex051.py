t1 = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA:'))
for contador in range(1,11):
    termo = t1 + (contador-1) * razão
    print(termo)