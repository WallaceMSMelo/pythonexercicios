extenso = ('zero', 'um', 'dois', 'trêis', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezssete', 'dezoito', 'dezenove', 'vinte')
while True:  # Solução do professor Guanabara
    numero = int(input("Digite um número de 0 a 20: "))
    if 0 <= numero <= 20:
        break
    print('Tente novamente!', end=" ")
print(f'Você digitou o numero {extenso[numero]}')

'''while True:  Minha Resolução
    c = numero = -1
    while numero not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20):
        if -1 < numero > 20:
            print('Tente novamente!', end=" ")
        numero = int(input("Digite um número de 0 a 20: "))
        for c in range(0, 21):
            if numero == c:
                print(f'Você digitou o numero {extenso[c]}')
    break'''
