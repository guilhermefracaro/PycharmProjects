frase = str(input('Digite uma frase: ')).strip().upper()
split = frase.split()
join = ''.join(split)
inverso = join[::-1]
print('O inverso de {} é {}'.format(join, inverso))
if inverso == join:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
