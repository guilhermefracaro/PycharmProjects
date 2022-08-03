from random import randint
tent = 1
comp = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
user = int(input('Qual é seu palpite? '))
while user != comp:
    if user < comp:
        print('Mais...Tente mais uma vez.')
        tent += 1
    else:
        print('Menos...Tente mais uma vez.')
        tent += 1
    user = int(input('Qual seu palpite? '))
print('Acertou com {} tentativas. Parabéns!'.format(tent))
