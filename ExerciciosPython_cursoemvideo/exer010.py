d = float(input('Quanto dinheiro você tem na carteira? R$ '))

print('Com essa quantia você poderá comprar US${: .2f}'.format(d/3.27))
print('Em 2022 consegue comprar os seguintes valores;')
print('Com R${: .2f} você consegue comprar US${: .2f}'.format(d, (d/5.09)))
print('Com R${: .2f} você consegue comprar EUR{: .2f}'.format(d, (d/5.24)))
