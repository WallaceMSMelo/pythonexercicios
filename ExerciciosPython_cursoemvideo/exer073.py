brasileirao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Arthletico-PR', 'Atlético-MG',
               'America-MG', 'Botafogo', 'São Paulo', 'Fortaleza', 'Bragantino', 'Goiás', 'Santos', 'Ceará', 'Cuiabá',
               'Atlético-GO', 'Avaí', 'Juventude')
print(f'Classificação do Campeonato Brasileiro:\n{brasileirao}')   # Solução do professor Guanabara
print('=-=' * 10)
print(f'Os 5 primeiros colocados:\n{brasileirao[0:5]}')

print('=-=' * 10)
print(f'Os 4 ultimos colocados:\n {brasileirao[-4:]}')

print('=-=' * 10)
print(f'Os times em ordem alfabetica colocados{sorted(brasileirao)}')
print('=-=' * 10)
print(f'O time Santos está na posição {brasileirao.index("Santos")+1}º')

''' Minha Resolução!

print(f'Classificação do Campeonato Brasileiro:\n{brasileirao}')
print('=-=' * 10)
for c in range(0, 5):
    print(brasileirao[c])
print('=-=' * 10)
for x in range(18, 14, -1):
    print(brasileirao[x])
print('=-=' * 10)
s = 0
while True:
    if 'Santos' in brasileirao[s]:
        print(f'O time Santos está na posição {s+1}º')
        break
    else:
        s += 1'''






