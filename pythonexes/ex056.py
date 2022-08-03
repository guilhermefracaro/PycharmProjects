totidade = 0
médiaidade = 0
hmaioridade = 0
hnomevelho = ''
mmenos20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    totidade += idade

    if p == 1 and sexo in 'M':
        hmaioridade = idade
        hnomevelho = nome
    if sexo in 'M' and idade > hmaioridade:
        hmaioridade = idade
        hnomevelho = nome

    if sexo in 'F' and idade < 20:
        mmenos20 += 1

médiaidade = totidade / 4
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(hmaioridade, hnomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mmenos20))
