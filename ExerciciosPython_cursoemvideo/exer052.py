num = int(input('Digite um número: '))
i = 0
for c in range(1, num + 1):
    if 0 == num % c:
        print('\033[1;33m{}\033[m'.format(c), end=' ')
        i += 1
    else:
        print('\033[1;31m{}\033[m'.format(c), end=' ')
if i <= 2:
    print('\nO número {} é \033[4mprimo\033[m, pois possui apenas {} divisores'.format(num, i))
elif i > 2:
    print('\nO número {} \033[4mnão é primo\033[m, pois possui {} divisores'.format(num, i))
