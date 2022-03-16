numeros = [[], []]
num = 0
for c in range(1, 8):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print(f'Todos os numeros inscritos foram: {numeros}')
numeros[0].sort()
numeros[1].sort()
print(f'Numeros pares inscritos foi: {numeros[0]}')
print(f'Numeros impares inscritos foi: {numeros[1]}')