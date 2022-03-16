from random import randint
lista = list()
jogos = list()
print('-='*20)
print('     NUMEROS DA MEGA SENA     ')
print('-='*20)
quant = int(input('Quantos jogos voce vai querer jogar: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'Sorteando {quant} jogos', '-='*3)
for i, l in enumerate(jogos):
    print(f'jogos {i+1}: {l}')

     