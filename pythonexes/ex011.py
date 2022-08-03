larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
tint = área / 2
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m²'.format(larg, alt, área))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format(tint))
