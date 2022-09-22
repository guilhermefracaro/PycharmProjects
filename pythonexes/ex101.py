def voto(anonasc):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - anonasc
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
