print('=-=')
print('O limite máximo permitido neste via e de 80 Km\h')
print('=-=')
v = int(input('Qual a velocidade do veículo? '))
if v >= 80:
    multa = v - 80
    print('Veículo multado por excesso de velocidade!\nTrafega a {}Km\h acima do limite permitido.'.format(multa))
    print('O valor de sua multa é R${: .2f}'.format(multa * 7))
    print('Dirija com mais cuidado, tenha um bom dia!')
else:
    print('O veículo está dentro do limite permitido!')
    print('Parabéns, continue mantendo a educação no trânsito')
