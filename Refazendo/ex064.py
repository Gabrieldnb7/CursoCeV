soma = total = num = 0
while num != 999:
    num = int(input('Digite um número[999 interrompe]: '))
    if num != 999:
        soma += num
        total += 1
print(f'Você digitou {total} números e a soma entre eles é {soma}')