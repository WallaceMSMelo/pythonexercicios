from math import trunc

# importando apenas a função TRUNC do modulo math
num = float(input('Digite um numero real: '))

print('A porção inteira do numero é {}'.format(trunc(num)))
# função interna do python 3 nao sendo necessários importar modulo algum
print(int(num))
