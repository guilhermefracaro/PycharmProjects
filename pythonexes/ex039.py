from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade > 18:
    print('Você já deveria ter se alistado há {} anos'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(nasc + 18))
elif idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
    print('Seu alistamento será em {}'.format(nasc + 18))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')