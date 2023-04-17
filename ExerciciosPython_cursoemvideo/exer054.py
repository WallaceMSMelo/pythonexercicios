import datetime
from datetime import date
i = 0
s = 0
v = date.today().year
for c in range(1, 8):
    dataNasc = int(input('Em que ano {}ª pessoa nasceu? '.format(c)))
    if v - dataNasc < 18:
        i += 1
    else:
        s += 1
print('Existe {} pessoas menores de idade'.format(i))
print('Existe {} pessoas maiores de idade'.format(s))
