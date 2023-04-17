# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
n1 = int(input('Digite o primeiro numero inteiro:'))
n2 = int(input('Digite o segundo numero inteiro:'))
n3 = float(input('Digite um numero Real'))

print('O resultado do produto do dobro do primeiro com metade do segundo é {}'.format((n1 * 2) + (n2 / 2)))
print('O resultado da soma do triplo do primeiro com o terceiro é {}'.format((n1 * 3) + 3))
print('O resultado do terceiro elevado ao cubo é {:.2f}'.format(pow(n3, 3)))

