# criando um programa que gera quantidade, media, maior e menor numero
cont = soma = maior = menor = 0
while True:
    # pedindo um numero
    num = int(input('Digite um numero: '))
    # contador para quantidade numeros digitados
    cont += 1
    # soma totalizando dos numeros inseridos
    soma += num
    # analisando qual e o maior e menor numero
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    # pergunto se deseja continuar ou nao
    d = str(input('Deseja Continuar [S/N]: ')).upper()
    if d in 'N':
        break
# calculando a media da totalidade dos numeros inseridos
media = soma / cont
# mostrando quantas numeros foi digitado, e a media deles
print(f'Voce digitou {cont} numeros e a media entre eles foi {media:.2f}')
# mostrando qual e o numero maior e menor numero
print(f'O maior numero digitado foi {maior} e menor numero digitado foi {menor}')
