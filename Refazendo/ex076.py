produtos = ('Processador Ryzen 5 7600x', 2329.99,
            'Memoria ddr5 6000hz', 899.99,
            'Placa mãe pica zen4', 2599.99,
            'Placa de video pica', 3799.99,
            'Fonte corsair modular sei la oque', 1199.29,
            'Water cooler RGB +30fps', 816.00,
            'Kit fan corsair', 649.99,
            )
print('-=-'*17)
print(f'{"Lista de preços":^50}')
print('-=-'*17)
for p in range(0, len(produtos)):
    if p % 2 == 0:
        print(f'{produtos[p]:.<40}',end='')
    else:
        print(f'R${produtos[p]:9.2f}')
print('-=-'*17)