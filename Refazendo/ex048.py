números = soma = 0
for contador in range (1, 501, 2): # forma que utiliza menos processamento
#for contador in range(1, 501): Forma que utiliza mais processamento
    if contador % 3 == 0: # contador % 2 == 1 (presente no processo que usa mais do computador)
        números += 1
        soma += contador
print(f'A soma dos {números} valores é {soma}')
