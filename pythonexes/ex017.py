from math import hypot
cop = float(input('Comprimento do cateto oposto: '))
cad = float(input('Comprimento do cateto adjacente: '))
hip = hypot(cop, cad)
print('A hipotenusa vai medir {:.2f}'.format(hip))
