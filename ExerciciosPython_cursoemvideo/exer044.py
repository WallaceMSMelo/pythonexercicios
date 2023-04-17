print('{:=^40}'.format(' LOJAS PYTHON'))
v = float(input('Digite o valor do produto: R$ '))
p = int(input('''Qual será a forma de pagamento;
[1] à vista/cheque;
[2] à vista no cartão;
[3] 2 vezes no cartão;
[4] 3 vezes ou mais no cartão;
Digite uma das opções:  '''))
if p == 1:
    print('O valor atual do produto é R${:.2f}\nO preço terá um DESCONTO de R${:.2f}\nValor total pelo produto é R$'
          '{:.2f}'.format(v, v * 0.10, v - (v * 0.10)))
elif p == 2:
    print('O valor atual do produto é R${:.2f}\nO preço terá um DESCONTO de R${:.2f}\nValor total pelo produto é R$'
          '{:.2f}'.format(v, v * 0.10, v - (v * 0.05)))
elif p == 3:
    parcelas = v / 2
    print('O valor do produto atual e R${:.2f}\nO valor de cada é R${:.2f} - SEM JUROS!\nValor total pelo produto é R$ '
          '{:.2f}'.format(v, parcelas, v))
elif p == 4:
    vezes = int(input('Quantas parcelas: '))
    parcelas = v / vezes
    print('O valor do produto atual e R${:.2f}\nO valor de cada é R${:.2f} - COM JUROS!\nValor total pelo produto '
          'é R$ {:.2f}'.format(v, parcelas, v + (v * 0.20)))
else:
    print('Favor digitar uma opção de pagamento válida!')
