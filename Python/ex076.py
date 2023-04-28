# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços organizando os dados em forma tabular.
listapc = (
    'Placa de vídeo pica', 3500.01, 'Gabinete brabo', 550.67, 'Processador AMD Ryzen', 1750.99, 'Processador i7 10k',
    2541.49, 'Placa Mãe Aorus pica', 815.98, 'Kit cooler RGBiba +30fps', 230.15, 'Watercooler com luizinha', 607.02,
    'Headset Gaymer', 529.41, 'Mouse gaymer 10000DPI', 249.99, 'Teclado Mecânico bonitão', 610.98)
print('_'*40)
print('{: ^40}'.format(('Listagem de Preços')))
print('_'*40)
print('{:.<30}R$ {:^8}'.format(listapc[0],listapc[1]))
print('{:.<30}R$ {:^8}'.format(listapc[2],listapc[3]))
print('{:.<30}R$ {:^8}'.format(listapc[4],listapc[5]))
print('{:.<30}R$ {:^8}'.format(listapc[6],listapc[7]))
print('{:.<30}R$ {:^8}'.format(listapc[8],listapc[9]))
print('{:.<30}R$ {:^8}'.format(listapc[10],listapc[11]))
print('{:.<30}R$ {:^8}'.format(listapc[12],listapc[13]))
print('{:.<30}R$ {:^8}'.format(listapc[14],listapc[15]))
print('{:.<30}R$ {:^8}'.format(listapc[16],listapc[17]))
print('{:.<30}R$ {:^8}'.format(listapc[18],listapc[19]))
print('_'*40)