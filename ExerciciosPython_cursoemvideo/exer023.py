num = int(input('Digite um numero de 0 a 9999'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidades: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhar: {}'.format(m))
#c = len(num)

#print(num[0:(len(num))])
#print('Unidades: {}'.format(num[len(num) - 1]))
#print('Dezenas: {}'.format(num[len(num) - 2]))
#print('Centenas: {}'.format(num[len(num) - 3]))
#print('Milhar: {}'.format(num[len(num) - len(num)]))
