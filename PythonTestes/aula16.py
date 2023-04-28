lanche = ('Hamburguer', 'Frango no pote', 'Sorvete', 'Coxinha')
for comida in lanche:
    print(f'Eu comi {comida}')
print('Comi pra caramba!')

## Ou também
for contador in range(0,len(lanche)):
    print(f'Comi {lanche[contador]} na posição {contador}') #talvez seja necessário enumerar as posições
print('Acabei comendo demais')

for pos, comida in enumerate(lanche):
    print(f'Eu comi {comida} na posição {pos}')