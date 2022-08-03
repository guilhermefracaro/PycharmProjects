br = ('Palmeiras', 'Corinthians', 'Fluminense', 'Athletico-PR', 'Flamengo',
      'Internacional', 'Atlético-MG', 'Bragantino', 'Santos', 'São Paulo',
      'Goiás', 'Botafogo', 'América-MG', 'Ceará', 'Coritiba',
      'Avaí', 'Cuiabá', 'Fortaleza', 'Atlético-GO', 'Juventude')
print(f'Tabela Brasileirão | 20º rodada {br}')
print('-' * 100)
print(f'Os 5 primeiros são {br[:5]}')
print('-' * 100)
print(f'Os 4 últimos são {br[-4:]}')
print('-' * 100)
print(f'Times em ordem alfabética {sorted(br)}')
print('-' * 100)
print('O Internacional está na {}º posição'.format(br.index('Internacional')+1))
