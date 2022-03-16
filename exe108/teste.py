import moeda
preço = float(input('Digite um valor: '))
print(f'A metade de R$:{moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'O dobro de R$:{moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preço, 10))}')
