s = ''
while s != 'MF':
    s = str(input('Digite seu sexo [M/F] ')).upper().strip()[0]
    if s == 'M':
        print('Masculino')
    elif s == 'F':
        print('Feminino')
    else:
        print('Digite um valor correto!')

''' Resposta do Professor
sexo = str(input('Informe se sexo: [M/F] ').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))'''