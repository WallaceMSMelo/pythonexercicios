n = int(input('Digite um numero: '))
j = 1
f = i = c = 0
while c < n:
    print(i, end=' => ')
    f = i + j
    i = j
    j = f
    c += 1
print('FIM')