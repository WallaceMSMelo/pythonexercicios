# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o
# salário líquido.
h = float(input('Quantas horas foram trabalhadas: '))
g = float(input('Quanto ganhar por hora: '))
salario = g * h
ir = salario * 0.11
inss = salario * 0.08
sin = salario * 0.05
print('Salário bruto R${: .2f}\nImposto de renda R${: .2f}\nINSS R${: .2f}\nSindicato R${: .2f}\nSalário liquido R$'
      '{: .2f}'.format(salario, ir, inss, sin, salario - ir - inss - sin))
