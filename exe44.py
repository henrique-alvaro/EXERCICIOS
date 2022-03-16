# pedindo preço de um produto
preço = float(input('Valor do produto: '))
# dando opções de pagamento para o cliente
print('''Escolha a Opçao de Pagamento
[ 1 ] - Á vista dinheiro/cheque
[ 2 ] - Á vista no cartão
[ 3 ] - Em até 2x no cartao
[ 4 ] - 3x ou mais no cartao''')
# pedindo qual e a opção va realizar o pagamento
opçao = int(input('Opção: '))
# analisando se a forma de pagamento vai ter desconto ou juros
if opçao == 1:
    valorf = preço - (preço * 10/100)
    print('Pamento á vista com Dinheiro ou cheque')
    print(f'Valor do Produto: R$:{preço}, á vista tem desconto de 10% fica: R$:{valorf}')
elif opçao == 2:
    valorf = preço - (preço * 5/100)
    print('Pagamento á vista com cartão')
    print(f'Valor do Produto: R$:{preço}, á vista no cartao tem desconto de 5% fica: R$:{valorf}')
elif opçao == 3:
    print('Dividin em 2x')
    print(f'Valor do Produto: R$:{preço}')
elif opçao == 4:
    valorf = preço + (preço * 20/100)
    print('Pagamento em 3x ou mais')
    print(f'Valor do Produto: R$:{preço}, com juros de 20% fica: R$:{valorf}')