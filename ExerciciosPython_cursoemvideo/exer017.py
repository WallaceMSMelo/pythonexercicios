from math import sqrt, hypot

co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
# utilizando a formula matematica direta junto do modulo math.SQRT para achar o resultado a hipotenusa
hi = sqrt((ca ** 2 + co ** 2)) # ou usar (CA ** 2 + CO **2) ** (1/2)

print(hi)
print('a hipotenusa dos catetos {} e {} é {:.2f}'.format(co, ca, hypot(co, ca)))
