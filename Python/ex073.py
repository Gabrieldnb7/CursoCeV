# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre: A) apenas os 5 primeiros colocados B) Os últimos 4 colocados da tabela C) Uma lista com
# os times em ordem alfabética D) Em que posição na tabela está o time da Chapecoense

brasileirao = (
    'Atlético-MG', 'Flamengo', 'Bragantino', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Internacional', 'Athleico-PR',
    'Fluminense', 'América-MG', 'Atlético-GO', 'Cuiabá', 'São Paulo', 'Ceará-SC', 'Santos', 'Juventude', 'Bahia',
    'Sport Recife', 'Grêmio', 'Chapecoense')
print(f'Os cinco primeiros colocados são: {brasileirao[:5]}')
print(f'Os quatro últimos colocados são: {brasileirao[16:]}')
print(f'Os times em ordem alfabética são:{sorted(brasileirao)}')
print(f'O time do(a) {brasileirao[19]} está na  {brasileirao.index("Chapecoense")+1}ª posição')

