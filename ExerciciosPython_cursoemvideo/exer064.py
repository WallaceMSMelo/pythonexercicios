n = r = s = c = 0
while n != 999:
    n = int(input('Digite um numero: '))
    if n != 999:
        r = n
        c += 1
        s = s + r
print('O total de numero digitados foi {} e a soma é {}'.format(c, s))
