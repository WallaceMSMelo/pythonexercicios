n1 = int(input('Digite um numero '))
n2 = int(input('Digite outro numero '))
if n1 > n2:
    print('O numero {} e maior\nO numero {} e o menor'.format(n1, n2))
elif n2 > n1:
    print('O numero {} e maior\nO numero {} e o menor'.format(n2, n1))
else:
    print('Não existe valor maior, pois os dois números são iguais')
print('Pronto!')
