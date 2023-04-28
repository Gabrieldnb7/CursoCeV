listapc = (
    'Placa de vídeo pica', 3500.01, 'Gabinete brabo', 550.67, 'Processador AMD Ryzen', 1750.99, 'Processador i7 10k',
    2541.49, 'Placa Mãe Aorus pica', 815.98, 'Kit cooler RGBiba +30fps', 230.15, 'Watercooler com luizinha', 607.02,
    'Headset Gaymer', 529.41, 'Mouse gaymer 10000DPI', 249.99, 'Teclado Mecânico bonitão', 610.98)
for posicao in range(0,len(listapc)):
    if posicao % 2 == 0:
        print(f'{listapc[posicao]:.<30}',end='')
    if posicao % 2 == 1:
        print(f'R$ {listapc[posicao]:>7.2f}')