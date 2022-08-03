real = float(input('Quanto dinheiro você tem na carteira: R$'))
dolar = real / 5.41
euro = real / 5.46
iene = real * 25.61
print('Com R${:.2f}, você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f}, você pode comprar €{:.2f}'.format(real, euro))
print('Com R${:.2f}, você pode comprar ¥{:.2f}'.format(real, iene))