numeros = ((int(input(f'Digite o um numero: '))), 
           (int(input(f'Digite outro numero: '))),
           (int(input(f'Digite mais um numero: '))), 
           (int(input(f'Digite o ultimo numero: '))))
print(f'O numero 9 apareceu {numeros.count(9)} vezes')
if 9 in numeros:
    print(f'O numero 3 apareceu na {numeros.index(3)+1}° posiçao')
print('Os valores pares digitados foram: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end='')