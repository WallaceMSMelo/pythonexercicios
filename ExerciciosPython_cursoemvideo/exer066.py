n = r = s = c = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    else:
        r = n
        c += 1
        s += r
print(f'A soma dos {c} valores foi {s}!')

