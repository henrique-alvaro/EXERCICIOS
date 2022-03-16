# pedindo valor de um produto
preço = float(input('Valor do produto: '))
# calculando o desconto do produto
desconto = preço - (preço * 5/100)
# mostrando valor do produto com desconto
print(f'Valor do produto: R$:{preço}, com desconto de 5% fica R$:{desconto:.2f}')
