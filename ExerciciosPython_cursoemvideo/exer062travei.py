ptermo = int(input('Digite o Primeiro termo'))
razao = int(input('Digite a razão: '))
termo = ptermo
c = 1
ntermo = 10
total = 0
while ntermo != 0:
    total = total + ntermo
    while c <= total:
        print(termo, end=' => ')
        termo += razao
        c += 1
    print('PAUSA')
    ntermo = int(input('\n Quantos termos você quer mostrar a mais? '))
print('Numero de termos foi '.format(total))