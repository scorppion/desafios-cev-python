peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / altura**2
if imc < 18.5:
    print('IMC: {:.2f}\nAbaixo do peso!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('IMC: {:.2f}\nPeso ideal!'.format(imc))
elif imc >= 25 and imc < 30:
    print('IMC: {:.2f}\nSobrepeso!'.format(imc))
elif imc >= 30 and imc < 40:
    print('IMC: {:.2f}\nObesidade!'.format(imc))
else:
    print('IMC:{:.2f}\nObesidade mórbida!')