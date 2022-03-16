# perguntando quanto de dinheiro voce tem
din = float(input('Dinheiro: '))
# fazendo as contas de quantos dolares voce pode comprar
dolar = din / 5.26
# mostrando o quanto voce pode comprar
print(f'Voce tem R$:{din} Reais, pode comprar $:{dolar:.2f} Dolares')
