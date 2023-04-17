from datetime import date
ano = int(input('Digite o ano de nascimento do alteta: '))
atual = date.today().year
idade = atual - ano
print('O atleta nasceu e {} e tem {} de idade.'.format(ano, idade))
if idade <= 9:
    print('Pertence a categoria: MIRIM')
elif idade <= 14:
    print('Pertence a categoria: INFANTIL')
elif idade <= 19:
    print('Pertence a categoria: JÚNIOR')
elif idade <= 25:
    print('Pertence a categoria: SÊNIOR')
else:
    print('Pertence a categoria: Master')
