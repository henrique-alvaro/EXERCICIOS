# pedindo o primeiro termo
primeiro = int(input('Primeiro Termo: '))
# pedindo uma razao
razao = int(input('Razao: '))
# termo recebe primeiro termo
termo = primeiro
# contador
cont = 1
# para somar o total de termos pedidos
total = 0
# quantos termos a mias voce vai querer que mostre sendo que ja mostrar 10 inicial
mais = 10
# enquanto no pedido por mais nao for inserido 0 nao vai terminar
while mais != 0:
    # somando o taotal de termos
    total += mais
    # enquanto o contador for menor ou igual ao total
    while cont <= total:
        # inserindo os termos pedidos
        print(f'{termo} -> ', end='')
        # somando os termos
        termo += razao
        # contador para finalizar o laço
        cont += 1
    print('PAUSA')
    # perguntando se ele quer mais termos
    mais = int(input('Voce quer quantos a mais: '))
# mostrando o total de termos
print(f'Foi inserido um total de {total} termos')
