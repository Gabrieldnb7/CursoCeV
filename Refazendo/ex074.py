from random import randint
números = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for indìce, num in enumerate(números):
   if indìce == 0:
       maior = menor = num
   else:
       if num > maior:
           maior = num
       if num < menor:
           menor = num
'''é possível fazer essa logica de maior e menor com outra função:
print(f'O maior valor sorteado foi max(números')
print(f'O menor valor sorteado foi min(números')'''
print(f'Os números sorteados foram: {números}\nO maior valor corresponde a {maior} e o menor corresponde a {menor}.')