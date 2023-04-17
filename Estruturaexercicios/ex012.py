altura = float(input('Digite o seu altura: '))

print('O sua altura informada foi: \033[1;33m{:.2f}\033[m\nE o seu peso ideal é \033[1;36m{:.1f}\033[m'.format(altura, 72.7 * altura - 58))
