tot = float(input('Qual o preço do produto? R$'))
desc = tot - (tot * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(tot, desc))
