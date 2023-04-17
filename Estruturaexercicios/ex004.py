# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
a = float(input('Insira a primeira nota: '))
b = float(input('Insira a segunda nota: '))
c = float(input('Insira a terceira nota: '))
d = float(input('Insira a quarta nota: '))
smedia = a + b + c + d
rmedia = smedia / 4
print('A media das notas {:.1f}, {:.1f}, {:.1f}, e {:.1f} é =  {:.2f}'.format(a, b, c, d, rmedia))


