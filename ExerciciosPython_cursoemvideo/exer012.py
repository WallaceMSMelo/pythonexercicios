preco = float(input('Digite o preço do produto: R$ '))
nvpreco = preco - (preco * 0.05)
# ou preco*5/100
print('O preço do produto era R${: .2f} e agora custa R${: .2f}'.format(preco, nvpreco))
