n = 1
qtdpar = 0
qtdimp = 0
while n != 0:
    n = int(input('Digite um valor [0 para parar]: '))
    if n != 0:
        if n % 2 == 0:
            qtdpar += 1
        else:
            qtdimp += 1
print('Você digitou {} números pares e {} números ímpares'.format(qtdpar, qtdimp))
