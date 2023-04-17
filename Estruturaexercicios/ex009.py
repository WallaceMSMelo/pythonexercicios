# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius
f = float(input('Digite a temperatura e Fº'))
c = 5 * ((f-32) / 9)
print('{:.1f}Fº equivale à {:.1f}Cº'. format(f, c))
