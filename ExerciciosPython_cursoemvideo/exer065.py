p = ''
n = c = s = maior = menor = 0
while p != 'N':
    n = int(input('Digite um numero: '))
    if c == 0:
        menor = maior = n
        c += 1
        s += n
    else:
        if c > 0:
            s += n
            c += 1
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    p = str(input('Quer continuar[S/N] ')).strip().upper()[0]
print('Você digitou {} números e a média é {:.2f}'.format(c, (s/c)))
print('O maior valor foi {} e o menor numero foi {} '.format(maior, menor))




