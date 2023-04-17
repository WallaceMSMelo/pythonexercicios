n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
# resolução do professor
# verificando o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# veficando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))


'''if n1 > n2 > n3: # OK
    print('{} e o maior numero'.format(n1))
    print('{} e o menor'.format(n3))
if n3 > n2 > n1: # OK
    print('{} e o maior'.format(n3))
    print('{} e o menor'.format(n1))
if n2 > n3 > n1: # OK
    print('{} e o maior'.format(n2))
    print('{} e o menor'.format(n1))
if n3 < n2 > n1: # ok
    print('{} e o maior'.format(n2))
    print('{} e o menor'.format(n3))
if n1 > n2 < n3:
    print('{} e o maior'.format(n1))
    print('{} e o menor'.format(n2))'''
