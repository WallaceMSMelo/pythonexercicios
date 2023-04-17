from math import radians, sin, cos, tan

# variavel tipo inteira recebe o valor do ângulo digitado
ang = int(input('Digite o ângulo: '))
# radians converte o angulo em radianos
print('O Seno é {:.2f}'.format(sin(radians(ang))))
print('O cosseno é {:.2f}'.format(cos(radians(ang))))
print('A tangente é {:.2f}'.format(tan(radians(ang))))
