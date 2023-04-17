a = float(input('Digite sua altura: '))
p = float(input('Digite seu peso: '))
imc = p / (a * a)
if imc <= 18.5:
    print('Seu IMC é {:.1f} você está abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.1f} você esta no peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.1f} você esta com sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.14f} você esta com obesidade'.format(imc))
else:
    print('Seu IMC é {:.1f} você esta no obesidade mórbida'.format(imc))
