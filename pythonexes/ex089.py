ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], média])
    op = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    op = int(input('Mostrar notas de qual aluno [999 interrompe]: '))
    if op == 999:
        print('FINALIZANDO...')
        break
    if op <= len(ficha) - 1:
        print(f'Notas de {ficha[op][0]} são {ficha[op][1]}')
