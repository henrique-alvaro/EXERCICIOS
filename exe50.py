# pedindo um valor aleatorio
soma = 0
# analisando se o numero e pares
# fazendo somatoria somente dos numeros pares
for c in range(0, 6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num
# mostrando numeros inseridos e calculando o total dos numeros pares
print(f'A soma dos valores pares e => {soma}')