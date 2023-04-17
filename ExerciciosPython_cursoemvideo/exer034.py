salario = float(int(input('Digite O valor de seu salário R$ ')))
if salario > 1250:
    novo = salario + (salario * 0.10)
    print('Seu salario atual e superior a R$ 1250,00')
    print('O seu salario atual e de R${: .2f}, terá um aumento de 10% sendo R${: .2f}'.format(salario, novo))
if salario <= 1250:
    novo = salario + (salario * 0.15)
    print('Seu salario atual e inferior a R$ 1250,00')
    print('Seu salario atual e de R${: .2f}, terá um aumento de 15% sendo R${: .2f}'.format(salario, novo))

    