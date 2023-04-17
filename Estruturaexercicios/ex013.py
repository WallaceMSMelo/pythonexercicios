# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas: Para homens: (72.7*h) - 58 Para mulheres: (62.1*h) - 44.7
altura = float(input('Digite sua altura: '))
genero = str(input('Qual o sexo? ')).strip().upper()

if genero == 'HOMEM':
    ideal = 72.7 * altura - 58
    print(
        'A sua altura informada foi \033[1;33m{:.2f}\033[m\nE o seu peso ideal é \033[1;36m{:.1f}\033[m'.format(altura,
                                                                                                                 72.7 * altura - 58))
if genero == 'MULHER':
    print(
        'A sua altura informada foi \033[1;33m{:.2f}\033[m\nE o seu peso ideal é \033[1;36m{:.1f}\033[m'.format(altura,
                                                                                                                62.1 * altura - 44.7))
