# Calcular e somar numeros impares multiplos de 3 entre 1 e 500
s = 0
i = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        i += 1  # e igual à escrever i = i + 1
        s += c  # e igual à escrever s = s + c
print('O somatório dos {} valores solicitados é {}'.format(i, s))
