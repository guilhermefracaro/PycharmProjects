from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 40)
print('{:^40}'.format('MEGA SENA'))
print('-' * 40)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= qtd:
    cont = 0
    while True:
        num = int(randint(1, 60))
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 4, f'SORTEANDO {qtd} JOGOS ', '-=' * 4)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 6, 'BOA SORTE', '-=' * 6)
