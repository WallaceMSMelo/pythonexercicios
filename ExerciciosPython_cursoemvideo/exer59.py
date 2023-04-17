total = m = n1 = n2 = 0
while m != 5:
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    print('=' * 10)
    m = int(input('''Menu de Opções:
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos números
[5]Sair do programa '''))
    print('=' * 10)
    if m <= 0 or m > 5:
        print('Digite um opção válida')
    if m == 1:
        print('O resultado é {}'.format(n1 + n2))
    elif m == 2:
        print('O resultado é {}'.format(n1 * n2))
    elif m == 3:
        if n1 == n2:
            print('{} é {} são Iguais!'.format(n1, n2))
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        if n1 < n2:
            print('{} é menor que {}'.format(n1, n2))
    elif m == 4:
        print('Digite novos numeros!')
print('Você encerrou o programa!')


