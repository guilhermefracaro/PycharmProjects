from random import randint
from time import sleep
print('-=' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=' * 30)
comp = randint(0, 5)
user = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if comp == user:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(comp, user))
