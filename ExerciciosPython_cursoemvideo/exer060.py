from math import factorial
n = int(input('digite um numero:'))
print('O fatorial de {}! é'.format(n), end=' ')
'''for c in range(n, 0, -1):
    if c == 1:
        print(c, end=' = ')
    else:
        print(c, end='x')
print(factorial(n))'''
s = n
while s != 0:
    if s == 1:
        print(s, end=' = ')
        s -= 1
    else:
        print(s, end='x')
        s -= 1
print(factorial(n))
