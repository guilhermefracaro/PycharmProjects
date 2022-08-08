matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maior = somacoluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
    print()
print('-=' * 30)
print('A soma dos valores pares é {}'.format(pares))
for linha in range(0, 3):
    somacoluna += matriz[linha][2]
print('A soma dos valores da terceira coluna é {}'.format(somacoluna))
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print('O maior valor da segunda linha é {}'.format(maior))
