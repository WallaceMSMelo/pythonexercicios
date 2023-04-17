from datetime import date

ano = int(input('Digite um ano para saber se e bixessto: digite 0 para pegar a data atual'))
if ano == 0:
    ano = date.today().year   # pega o ano atual
if ano % 4 == 0 and ano % 100 or ano % 400 == 0:
    print('{} é um ano bixessto!'.format(ano))
else:
    print('{} não e um ano bixessto!'.format(ano))
