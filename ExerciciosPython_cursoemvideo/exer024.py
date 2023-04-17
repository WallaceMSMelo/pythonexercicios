frase = str(input('Digite o nome de uma cidade: ')).strip()
pnome = frase.split()
nvnome = pnome[0].upper()
#print(nvnome)
print(nvnome.find("SANTO"))
print('SANTO' in nvnome)

#professor
print(frase[0:5].upper() == 'SANTO')
