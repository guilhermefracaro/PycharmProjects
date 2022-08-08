valores = []
pares = []
ímpares = []
while True:
    valores.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
