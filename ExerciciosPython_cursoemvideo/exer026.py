frase = str(input('Digite uma frase')).upper().strip()
print('A frase digitada possui {} ocorrências da palavra (A).'.format(frase.count('A')))
print('Primeira ocorrência no índice: {}'.format(frase.find('A') + 1))
print('Ultima ocorrência no índice: {}'.format(frase.rfind('A') + 1))





