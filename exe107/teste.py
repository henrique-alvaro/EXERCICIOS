import moeda

preço = float(input('Digite um valor: '))
print(f'A metade de R$:{preço} é {moeda.metade(preço)}')
print(f'O dobro de R$:{preço} é {moeda.dobro(preço)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preço, 10)}')