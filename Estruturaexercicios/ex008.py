# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês
custohora = float(input('Quanto você ganha por hora ? '))
hdia = float(input('Quantidade de horas diarias ? '))


def cal(a, b):
    c = float(a * b)
    print("O seu sálario mensal é: R${: .2f}".format(c * 22))


cal(custohora, hdia)
