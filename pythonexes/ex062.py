print('-=' * 12)
print('Gerador de PA')
print('-=' * 12)
pt = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
termo = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += raz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos registrados'.format(total))
