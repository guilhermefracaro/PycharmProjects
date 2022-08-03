maior18 = totH = totM20 = 0
while True:
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    if idade >= 18:
        maior18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if sexo == 'M':
            totH += 1
        if sexo == 'F' and idade < 20:
            totM20 += 1
    print('-' * 20)
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        print('-' * 20)
    if op == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {totH} homen(s) cadastrados')
print(f'E temos {totM20} mulhere(s) com menos de 20 anos')
