t = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
c = 0
while c < 10:
    if c < 10:
        print(t, end=' => ')
        t += r
        c += 1

print('FIM')