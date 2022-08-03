total = tot1000 = menor = cont = 0
barato = ''
while True:
    nome = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço >= 1000:
        tot1000 += 1
    if cont == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {tot1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
