# criando um para pedir numeros
# no final mostrar quantos numeros foi digitado e o total inseridos
cont = soma = n = 0
# pedindo varios numeros
n = int(input('Digite um numero [999 para interromper]: '))
# enquanto numero inserido nao for 999 nao vai parar
while n != 999:
    # contador para saber quantos numeros foi inseridos
    cont += 1
    # somando total dos numeros
    soma += n
    # pedindo novamente um numero
    n = int(input('Digite um numero [999 para interromper]: '))
# mostrando quantidade de numeros, e o total que eles ao todo soma
print(f'Voce digitou {cont} numeros e a soma entre eles foi {soma}')
