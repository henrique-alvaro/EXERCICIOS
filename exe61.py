# pedindo primeiro termo
primeiro = int(input('Primeiro Termo: '))
# pedindo a razao
razao = int(input('Razao: '))
# termo igual ao primeiro termo
termo = primeiro
# criando um contador
cont = 1
# enquanto o contador for menor que 10 vai continuar contando
while cont <= 10:
    # mostrando os termos
    print(f'{termo} -> ', end='')
    # calculando os termos
    termo = termo + razao
    # contador
    cont += 1
print('Fim')