for cont in range(1, 51):  # Realiza o exercicio utilizando um condicional IF (desgaste de processamento)
    if (cont % 2) == 0:
        print(cont, end=' ')
print('FIM')

for c in range(2, 51, 2):  # Realiza o exercicio utilizando de 2 em 2 passos no contador (economiza processamento)
    print(c, end=' ')
print('FIM')
