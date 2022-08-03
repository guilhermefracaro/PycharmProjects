from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tang = tan(radians(ang))
print('O ângulo de {:.1f}° tem o seno de {:.2f}'.format(ang, seno))
print('O ângulo de {:.1f}° tem o seno de {:.2f}'.format(ang, cos))
print('O ângulo de {:.1f}° tem o seno de {:.2f}'.format(ang, tang))
