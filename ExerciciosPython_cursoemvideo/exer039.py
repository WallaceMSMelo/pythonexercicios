from datetime import datetime

ano = int(input('Olá, jovem! Digite o ano de seu nascimento '))
genero = str(input('Aperte (M) masculino e (F) Feminino: ')).lower()
atual = datetime.now()
idade = atual.year - ano
print('Você nasceu em {} e tem {} anos em {}'.format(ano, idade, atual.year))
if genero == 'f':
    print('Você não precisa fazer o alistamento militar')
elif idade == 18:
    print('Procure uma agência militar IMEDIATAMENTE!')
elif idade > 18:
    print('Já deveria ter se alistado há {} anos.\nSeu alistamento deveria ocorrer em {}.!'.format(idade - 18, atual.
                                                                                                   year - 18))
else:
    print('Faltam {} anos para seu alistamento militar.\nSeu alistamento será em {} '.format(18 - idade,  atual.year +
                                                                                             idade))
    