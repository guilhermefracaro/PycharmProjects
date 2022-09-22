from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
anoatual = datetime.now().year
anonasc = int(input('Ano de nascimento: '))
dados['idade'] = anoatual - anonasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - anoatual)
print('-=' * 30)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')
