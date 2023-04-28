t1 = int(input('Digite o primeiro valor da PA: '))
razão = int(input('Digite a razão da PA: '))
décimo = t1 + (10 - 1) * razão
for contador in range (t1, décimo + razão, razão):
    print(f'{contador}')