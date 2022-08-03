distkm = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.2f}Km'.format(distkm))
if distkm <= 200:
    preço = distkm * 0.5
else:
    preço = distkm * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
