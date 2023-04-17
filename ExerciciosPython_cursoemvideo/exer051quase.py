num = int(input('digite o primeiro numero da PA: '))
r = int(input('digite a razão: '))
dez = num + (10 - 1) * r
for c in range(num, dez + r, r):
    print(c, end=' -> ')
print('FIM')

