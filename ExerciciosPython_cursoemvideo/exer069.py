h = c = m = 0
print('-' * 20)
print('CADASTRE UMA PESSOA ')
print('-' * 20)
while True:  # Tirar esse for e utilizar while
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo: [M/F]: ')).strip().upper()[0]
        print('-' * 20)
    p = ' '
    while p not in 'SN':
        p = str(input('Quer Continuar?')).strip().upper()[0]
        print('-' * 20)
        if p == 'N':
            break
        if idade >= 18:
            c += 1
        if sexo in 'M':
            h += 1
        if sexo in 'F' and idade < 20:
            m += 1
print(f'Total de pessoas com mais de 18 anos : {c}')
print(f'Ao todo temos {h} homens cadastrados')
print(f'Temos {m} de mulheres abaixo dos 20 anos')
