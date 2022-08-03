qtdia = int(input('Quantos dias alugados? '))
qtkm = float(input('Quantos Km rodados? '))
vtot = (qtdia * 60) + (qtkm * 0.15)
print('O total a pagar é de R${:.2f}'.format(vtot))
