numero = int(input('Digite um numero inteiro: '))
base = int(input('Qual base de conversão? (1) para binário, (2) para octal e (3) para hexadecimal. '))
if base == 1:
    print('O numero convertido é: {}'.format(bin(numero)[2:]))
elif base == 2:
    print('O numero convertido é: {}'.format(oct(numero)[2:]))
elif base == 3:
    print('O numero convertido é: {}'.format(hex(numero)[2:]))
else:
    print('Base inválida')
