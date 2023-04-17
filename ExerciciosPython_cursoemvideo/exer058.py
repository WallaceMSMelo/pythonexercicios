from random import randint
computador = randint(0, 10)
c = jogador = 0
while computador != jogador:
    jogador = int(input('Digite um numero de 0 até 10: '))
    c += 1
    if jogador < 0 or jogador > 10:
        print('Digite um valor valido')
    elif computador == jogador:
        print('Parabens vc acertou!')
    else:
        if c == 1:
            print('Infelizmente você errou!')
        if c > 1:
            print('Infelizmente você errou de novo.')

print('Você precisou de {} tentativas para acertar!'.format(c))
