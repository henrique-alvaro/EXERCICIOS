# pedindo valor da casa, salario e o tempo de parcelamneto
casa = float(input('Valor da casa: '))
salario = float(input('Salario: '))
anos = int(input('Quantos de financiamento: '))
# calculando valor de prestaçao mensal
prestaçao = casa / (anos * 12)
# calculando os 30% de salario permitido por prestação
aprovaçao = salario * 30/100
# colocando o valor da casa tempo em anos,
# e o valor que vai ficar a prestação mensal
print(f'Para pagar R$:{casa} em {anos}. parcela fica {prestaçao:.2f}')
# analisando se os 30% do salario é maior que a prestação para aprovar o emprestimo
if prestaçao > aprovaçao:
    print(f'Emprestimo NEGADO, parcela excede valor de R$:{aprovaçao} do salario')
else:
    print('Emprestimo APROVADO!')
