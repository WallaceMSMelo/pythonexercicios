maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        menor = maior
    else:
        if peso > maior:
            menor = maior
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {:.1f}KG'.format(maior))
print('O menor peso é {:.1f}KG'.format(menor))
