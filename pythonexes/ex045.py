from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
comp = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
user = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 15)
print('Computador jogou {}'.format(itens[comp]))
print('Jogador jogou {}'.format(itens[user]))
print('-=' * 15)
if comp == 0: # computador jogou PEDRA
    if user == 0:
        print('EMPATE!')
    elif user == 1:
        print('JOGADOR VENCE!')
    elif user == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('Jogada inválida!')
elif comp == 1: # computador jogou PAPEL
    if user == 0:
        print('COMPUTADOR VENCE!')
    elif user == 1:
        print('EMPATE!')
    elif user == 2:
        print('JOGADOR VENCE!')
    else:
        print('Jogada inválida!')
elif comp == 2: # computador jogou TESOURA
    if user == 0:
        print('JOGADOR VENCE!')
    elif user == 1:
        print('COMPUTADOR VENCE!')
    elif user == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida!')
