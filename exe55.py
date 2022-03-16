# analisando peso
maior = 0
menor = 0
for c in range(1, 6):
    # pedindo o peso de uma pessoa
    peso = float(input('Digite seu Peso: '))
    # analisando maior e menor peso das pessoas cadastradas
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
# mostrando o maior peso
print(f'O maior peso escrito foi: {maior}kg')
# mostrando e menor peso
print(f'O menor peso escrito foi: {menor}kg')

