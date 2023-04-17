i = 0
maior = 0
media = 0
velho = ' '
for c in range(1, 5):
    print('-----{}ª PESSOA-----'.format(c))
    nome = str(input('Digite o nome: ')).capitalize().strip()
    sexo = str(input('Digite seu sexo: [F] ou [M]: ')).strip()
    idade = int(input('Digite sua idade:'))
    if c == 1 and sexo in 'Mm':
        maior = idade
        velho = nome
    if sexo in 'Ff' and idade < 20:
        i += 1
    if sexo in 'Mm' and idade > maior:
        maior = idade
        velho = nome
    if c < 5:
        media = media + idade

print('O nome do homem mais velho é {} e ele tem {} anos.'.format(velho, maior))
print('Temos {} de mulheres abaixo dos 20 anos'.format(i))
print('A média de idade do grupo é {}'.format(media / c))
