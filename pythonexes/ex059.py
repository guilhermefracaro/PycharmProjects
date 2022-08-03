from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    op = int(input('>>>>> Qual é a sua opção? '))
    if op == 1:
        print('O resultado de {} + {} é {}'.format(n1, n2, n1+n2))
    elif op == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1*n2))
    elif op == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n1))
        elif n2 > n1:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n2))
        else:
            print('Os valores são iguais')
    elif op == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
