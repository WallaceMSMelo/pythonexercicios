vinte = dez = dois = cinco = cinquenta = cem = c = 0
while True:
    valor = float(input('Digite o valor que vc quer sacar? R$ '))
    resto = -1
    if c == 0:
        cem = valor // 100
        resto = valor % 100
        c += 1
    if resto != 0:
        cinquenta = resto // 50
        resto50 = resto % 50
    if resto50 != 0:
        vinte = resto50 // 20
        resto20 = resto50 % 20
    if resto20 != 0:
        dez = resto50 // 10
        resto10 = resto20 % 10
    if resto10 != 0:
        cinco = resto10 // 5
        resto5 = resto10 % 5
    break
print(f'Total de {cem:.0f} de R$100')
print(f'Total de {cinquenta:.0f} de R$50')
print(f'Total de {vinte:.0f} de R$20')
print(f'Total de {dez:.0f} de R$10')
print(f'Total de {cinco:.0f} de R$5')
