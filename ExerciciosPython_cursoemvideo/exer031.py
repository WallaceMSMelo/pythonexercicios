distancia = float(input('Qual a distância deseja viajar: '))
'''if distancia <= 200:
    valor = distancia * 0.50
    print('Sua viagem de {:.1f}KM terá um total de R${: .2f}.'.format(distancia, valor))
else:
    valor = distancia * 0.45
    print('Sua viagem de {:.1f}KM terá um total de R$ {: .2f}.'.format(distancia, valor))'''
valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45  # If simplificado
print('Sua viagem de{: .1f}KM terá um custo total de R${: .2f}'.format(distancia, valor))
