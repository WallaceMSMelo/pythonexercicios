# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
c = float(input('Digite uma temperatura e Cº'))
f = ((c * 9) / 5) + 32
print('{:.1f}Cº equivale à {:.1f}Fº'.format(c, f))
