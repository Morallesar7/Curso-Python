# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da Chapecoense.

times = ('Corithias', 'Palmeiras', 'Santos', 'Grêmio',
        'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
        'Atletico', 'Botafogo', 'Atletico-PR', 'Bahia',
        'São Paulo', 'Fluminss', 'Sport', 
        'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
        'Atletico-Go')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[:-4]}')
print('-=' * 15)
print('')
