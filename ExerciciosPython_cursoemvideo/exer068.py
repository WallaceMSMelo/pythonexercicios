from random import randint
v = 0
while True:
    c = randint(0, 10)
    p = int(input('digite um valor: '))
    s = c + p
    j = ' '
    while j not in 'PI':
        j = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    if s % 2 == 0 and j in 'P':
        print(f'Você jogou {p} e o computador {c}. Total de {s} DEU PAR')
        print('VOCÊ VENCEU')
        v += 1
        print('Vamos jogar novamente...')
    elif s % 2 == 0 and j in 'I':
        print(f'Você jogou {p} e o computador {c}. Total de {s} DEU PAR')
        print('VOCÊ PERDEU')
        break
    elif s % 2 != 0 and j in 'P':
        print(f'Você jogou {p} e o computador {c}. Total de {s} DEU IMPAR')
        print('VOCÊ PERDEU')
        break
    elif s % 2 != 0 and j in 'I':
        print(f'Você jogou {p} e o computador {c}. Total de {s} DEU IMPAR')
        print('VOCÊ VENCEU')
        v += 1
        print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')
