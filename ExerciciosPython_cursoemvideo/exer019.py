from random import choice
# o valores digitados serão convertidos em string
a1 = str(input('Digite o primeiro aluno: '))
a2 = str(input('Digite o segundo aluno: '))
a3 = str(input('digite o terceiro aluno: '))
a4 = str(input('digite o quarto aluno: '))
# lembre-se sempre de colocar todos os resultados libidos em uma valiavel lista fica dentro de [ ]
lista = [a1, a2, a3, a4]
print('O nome do aluno sorteado foi {}'.format(choice(lista)))
