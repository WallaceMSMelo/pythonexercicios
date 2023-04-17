frase = str(input('Digite um frase')).strip().split()
i = 0
nova = ''.join(frase)
s = len(nova) - 1
print('O inverso de \033[32m{}\033[m é \033[34m{}\033[m'.format(nova, (nova[len(nova):: -1])))

'''if nova in nova[len(nova):: -1]:
    print('É um palíndromo!')   Podemos deixar de usar o laço FOR apenas usando essa condicional IF e ELSE
else:
    print('Não é um palíndromo.')'''

for c in range(len(nova), 0, -1):
    if nova[i] == nova[s]:
        # print(nova[i], end=' ') conta letra por letra sentido esq a dir
        i += 1
        s -= 1
    else:
        # print(nova[s], end=' ')  conta letra por letra sentido esq a dir
        i += 1
        s -= 1
if nova in nova[len(nova):: -1]:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo.')


