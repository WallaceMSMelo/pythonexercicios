valor = float(input('Qual o valor do imovel: R$ '))
salario = float(input('Quanto e o seu salario: R$ '))
tempo = int(input('Quanto tempo? '))
parcela = valor / (tempo * 12)

if parcela > salario * 0.30:
    print('=-=' * 10)
    print('Valor solicitado R${: .2f}\nValor de parcelas R${: .2f} '.format(valor, parcela))
    print('Emprestimo não pode ser efetuado, pois excede limite 30% de seu salario!')
    print('=-=' * 10)
else:
    print('=-=' * 10)
    print('Valor solicitado R${: .2f}\nValor de parcelas R${: .2f}\nTotal de parcelas {} meses'.format(valor, parcela, tempo * 12))
    print('Emprestimo liberado!')
    print('=-=' * 10)


