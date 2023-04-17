c = 1
n = 0
while True:
    if c == 1:
        n = int(input('Digite um numero para ver sua tabuada: '))
        print('-' * 20)
    if n < 0:
        break
    if c < 10:
        c += 1
        print(f'{n} x {c} = {n * c}')
    else:
        c = 1
        print('-' * 20)


print('PROGRAMA DE TABUADA ENCERRADO. Volte Sempre!')
