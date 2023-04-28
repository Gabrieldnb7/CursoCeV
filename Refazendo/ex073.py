Brasileirão = ('Palmeiras', 'Fluminense', 'Internacional', 'Corinthians', 'Flamengo', 'Athletico Paraense',
               'Atlético-MG', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'São Paulo', 'Bragantino',
               'Fortaleza', 'Coritiba', 'Ceará-SC', 'Cuiabá', 'Avaí', 'Atlético-GO', 'Juventude')
print(f'Os primeiros colocados são: {Brasileirão[0:5]}')
#print(f'Os primeiros colocados são:\n1º {Brasileirão[0]}\n2º {Brasileirão[1]}\n3º {Brasileirão[2]}\n4º {Brasileirão[3]}\n5º {Brasileirão[4]}')
print('-='*30)
print(f'Os Quatro últimos são: {Brasileirão[-4:]}')
#print(f'os Quatro últimos são:\n17º {Brasileirão[-4]}\n18º {Brasileirão[-3]}\n19º {Brasileirão[-2]}\n20º {Brasileirão[-1]}')
print('-='*30)
print(f'Os times em ordem alfabética são: {sorted(Brasileirão)}')
print('-='*30)
print(f'O time do Fortaleza está na posição {Brasileirão.index("Fortaleza")+1}')