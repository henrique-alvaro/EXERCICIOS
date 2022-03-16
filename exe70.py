total = tot1000 = menor = cont = 0
barato = ''
while True:
    produto = str(input('Digite um nome: '))
    preço = float(input('Preçodo Produto: '))
    cont += 1
    total += preço
    if preço >= 1000:
        tot1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    d = ' '
    while d not in 'SN':
        d = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
    if d == 'N':
        break
print(f'Valor total dos Produtos: R$:{total}')
print(f'Teve {tot1000} produto que custam mais de R$:1000 reais')
print(f'O produto mais barato foi {barato} e tem o valor de R$:{menor} ')
    
    
    