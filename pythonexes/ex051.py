print('=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('=' * 30)
ini = int(input('Primeiro Termo: '))
raz = int(input('Razão: '))
fim = ini + (10 - 1) * raz
for c in range(ini, fim + raz, raz):
    print(c, end=' - ')
print('ACABOU')
