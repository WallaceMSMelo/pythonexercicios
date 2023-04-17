from time import sleep
from random import randint
jogada = int(input('''Escolha as opções;
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual sua jogada? '''))

if 0 <= jogada <= 2:
    lista = ['Pedra', 'Papel', 'Tesoura']
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    comp = randint(0, 2)
    print('-=' * 20)
    print('\033[35mComputador\033[m jogou {} e \033[32mJogador\033[m jogou {}'.format(lista[comp], lista[jogada]))
    if jogada != comp:

        if jogada == 0 and comp == 1 or jogada == 1 and comp == 2 or jogada == 0 and comp == 2:
            print("\033[35mComputador\033[m Ganhou!!!")
        elif comp == 0 and jogada == 1 or comp == 1 and jogada == 2 or comp == 0 and jogada == 2:
            print('\033[32mJogador\033[m Ganhou!!!')
    else:
        print('\033[34mHouve um empate\033[m')
    print('-=' * 20)
else:
    print('-=' * 20)
    print('\033[30:47mOpção inválida! Digite novamente.\033[m')
    print('-=' * 20)
