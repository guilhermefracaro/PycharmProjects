n = str(input('Digite seu nome completo: ')).strip().upper()
print('Muito prazer em te conhecer!')
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0].capitalize()))
print('Seu último nome é {}'.format(nome[len(nome)-1].capitalize()))