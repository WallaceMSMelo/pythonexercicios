a = int(input('Digite um numero da tabuada de 1 a 10: '))

print('Segue abaixo a tabuada de {}\n----------\n{} X 1 = {}\n{} X 3 = {}\n{} X 3 = {}\n{} X 4 = {}\n{} X 5 = {}\n{} X 6 = {}\n{} X 7 = {}\n{}X8 = {}\n{'
      '}X9 = {}\n----------'.format(a, a, (a*1), a, (a*2), a, (a*3), a, (a*4), a, (a*5), a, (a*6), a, (a*7), a, (a*8), a, (a*9)))
#outra forma de se fazer a tabuada;
print('{} x {:2} = {}'.format(a, 1, (a*1)))