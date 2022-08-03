print('-=' * 12)
print('Gerador de PA')
print('-=' * 12)
pt = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
termo = pt
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += raz
    cont += 1
print('FIM')
