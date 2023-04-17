# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
p = int(input('Seu quadrado tem os lados iguais? Digite 1(SIM) e 2 (NÃO)'))

if p == 1:
    a = float(input('Qual o tamanho de cada lado? '))
    print('O seu quadrado possui uma área de {:.2f}'.format(a ** 2))
else:
    a = float(input('Digite o tamanho da altura ? '))
    b = float(input('Digite o tamanho da base? '))
    print('O seu quadrado possui uma área de {:.2f}'.format(a * b))
