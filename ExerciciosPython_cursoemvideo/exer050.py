s = 0
i = 0
for cont in range(0, 6):
    n = int(input('Digite um numero:'))
    if n % 2 == 0:
        s = s + n
        i = i + 1
print('você informou {} PARES e o somatório é {}'.format(i, s))
