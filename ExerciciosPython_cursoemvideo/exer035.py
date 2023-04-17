a = float(input('Digite o tamanho da primeira reta: '))
b = float(input('Digite o tamanho da segunda reta: '))
c = float(input('Digite o tamanho da terceira reta: '))

if a + b > c and c + b > a and a + c > b:
    print('\033[4;31mÉ possível formar um triângulo\033[m')
else:
    print('\033[1;31mNão é possível formar um triângulo\033[m')
