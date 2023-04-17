r1 = float(input('Digite o tamanho da reta 1: '))
r2 = float(input('Digite o tamanho da reta 2: '))
r3 = float(input('Digite o tamanho da reta 3: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Essas retas foram um triângulo')
    if r2 == r1 == r3:  # tive dificuldade em realizar e entender os if's aninhados dentro de outro if's
        print('Foram um equilátero')
    elif r1 != r2 != r3 != r1:
        print('Formam um escaleno')
    else:
        print('Formam um isósceles')
else:
    print('Não formam um triângulo')
