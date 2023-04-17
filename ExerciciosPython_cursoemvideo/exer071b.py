vinte = dez = dois = cinco = cinquenta = c = 0
resto50 = resto20 = resto10 = resto5 = resto2 = 0
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
while True:
    valor = float(input('Digite o valor que vc quer sacar? R$ '))
    cem = valor // 100
    resto = valor % 100
    if cem != 0:
        print(f'Total de {cem:.0f} de R$100')
    if resto != 0:
        cinquenta = resto // 50
        resto50 = resto % 50
        if cinquenta != 0:
            print(f'Total de {cinquenta:.0f} de R$50')
    if resto50 != 0:
        vinte = resto50 // 20
        resto20 = resto50 % 20
        if vinte != 0:
            print(f'Total de {vinte:.0f} de R$20')
    if resto20 != 0:
        dez = resto20 // 10
        resto10 = resto20 % 10
        if dez != 0:
            print(f'Total de {dez:.0f} de R$10')
    if resto10 != 0:
        cinco = resto10 // 5
        resto5 = resto10 % 5
        if cinco != 0:
            print(f'Total de {cinco:.0f} de R$5')
    if resto5 != 0:
        dois = resto5 // 2
        resto2 = resto5 % 2
        if dois != 0:
            print(f'Total de {dois:.0f} de R$2')
    break
