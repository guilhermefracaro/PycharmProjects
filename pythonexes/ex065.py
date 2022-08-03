resp = 'S'
cont = tot = med = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    tot += num
    cont += 1
    med = tot / cont
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('Você digitou {} números e a média foi {}'.format(cont, med))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
