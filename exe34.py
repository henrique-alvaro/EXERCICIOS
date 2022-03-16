# pedindo valor de um salario
salario = float(input('Salario: '))
# analisando se salario e miaor ou menor de 1250,
# caso seja maior de 1250 receber 10% de aumento,
# ou caso seja menor de 1250 receber 15% de aumento.
if salario <= 1250:
    aumento = salario + (salario * 15/100)
    print(f'Salario do funcioanrio e R$:{salario}, com aumento de 15% vai ficar R$:{aumento}')
else:
    aumento = salario - (salario * 10/100)
    print(f'Salario do funcionario e R$:{salario}, com aumento de 10% vai ficar R$:{aumento}')

