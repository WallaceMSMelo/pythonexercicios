menor = c = quant = total = 0
barato = ' '
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço: '))
    perg = ' '
    if c == 0:
        menor = preco
        c += 1
    total = total + preco
    while perg not in 'SN':
        perg = str(input('Quer continuar?')).strip().upper()[0]
    if perg == 'N':
        break
    if preco > 1000:
        quant += 1
    if preco < menor:
        menor = preco
        barato = nome

print('')
print(f'O total da compra foi {total:.2f}')
print(f'Temos {quant} produtos custam mais e R$1000.00')
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}")



