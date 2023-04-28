Km = float(input('Quantos quilômetros foram percorridos? '))
dias = int(input('Por quantos dias foi alugado? '))
total = (Km*0.15) + (dias*60)
print(f'O valor total a pagar é R${total:.2f}.')