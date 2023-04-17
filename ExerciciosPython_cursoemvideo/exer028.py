from random import randint
from time import sleep
print('-=-' * 10)
print('Tente acertar qual numero o computador esta pensado!')
print('-=-' * 10)

n = int(input('Tente acertar um numero de 1 a 5: '))  # usuario tenta adivinhar
print('Verificando...')
sleep(2)  # faz o computador dar um atraso na resposta
n2 = randint(1, 5)  # faz o computador escolher um numero aleatorio
if n2 == n:
    print('Computador: {}\nUsuário: {}\nVocê acertou, Parabéns!'.format(n2, n))

else:
    print('Computador: {}\nUsuário: {}\nVocê errou, tente novamente.'.format(n2, n))
