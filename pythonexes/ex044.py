print('{:^40}'.format(' 👽👽👽👽👽 '))
compra = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
op = int(input('Qual sua opção? '))
if op == 1:
    total = compra - (compra * 10 / 100)
elif op == 2:
    total = compra - (compra * 5 / 100)
elif op == 3:
    total = compra
    totparcelado = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(totparcelado))
elif op == 4:
    total = compra + (compra * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    totparcelado = total / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, totparcelado))
else:
    total = compra
    print('Digite uma opção válida!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(compra, total))
