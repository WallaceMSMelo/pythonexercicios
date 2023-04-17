nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome completo em maiúsculo é', nome.upper())
print('Seu nome completo em minúsculo é', nome.lower())
print('Seu nome possui {} espaços'.format(len(nome) - nome.count(' ')))
pnome = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(pnome[0], len(pnome[0])))
print('Seu nome tem {} letras '.format(nome.find(' ')))

