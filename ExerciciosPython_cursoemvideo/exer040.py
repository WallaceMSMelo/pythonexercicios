n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Média abaixo de 5: REPROVADO.')
elif 5 <= media < 7:
    print('Média entre 5 e 6.9: RECUPERAÇÃO')
elif media > 7.0:
    print('Média 7.0 ou superior: APROVADO')
    