# criando uma sequencia de fibonacci
# o proximo numero e sempre a soma dos 2 anteriores
print('Seguencia de Finonacci')
print('--'*20)
# pedindo um numero
n = int(input('Quantos termos voce quer mostrar: '))
# primeiro termo
t1 = 0
# segundo termo
t2 = 1
# mostrando os 2 primerios termos
print(f'{t1} -> {t2}', end='')
# contador apartir de 3 porque ja tem dois termos iniciais
cont = 3
# enquanto o contador for menor que o numero pedido vai continuar
while cont < n:
    # terceiro termo e a soma dos 2 anteriores
    t3 = t1 + t2
    # mostrando o terceiro termo
    print(f' -> {t3}', end='')
    # contador para finalizar o laço
    cont += 1
    # fazendo sequencialmente a troca de posiçoes para somar
    t1 = t2
    t2 = t3
print(' -> Fim')