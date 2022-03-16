# pedindo altura 
altura = float(input('Altura: '))
# pedindo peso
peso = float(input('Peso: '))
# fazendo o calculo do imc
imc = peso / (altura * altura)
# analisando imc para ver se estar abaixo, acima ou no peso ideal
if imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 < imc <= 25:
    print('Peso Ideal')
elif 25 < imc <= 30:
    print('Sobre Peso')
elif 30 < imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')
