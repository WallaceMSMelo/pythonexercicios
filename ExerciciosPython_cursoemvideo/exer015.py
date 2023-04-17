km = float(input('Quantos KM foram percorridos? '))
dia = int(input('Quantos dias de aluguel? '))
print('O valor cobrado sera de : R$ {:.2f}'.format(km * 0.15 + dia * 60))
