pessoas = {'nome': 'Andrew', 'sexo': 'M', 'idade': 36}
pessoas['nome'] = 'Chris'
pessoas['peso'] = 86.5
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} - {v}')
