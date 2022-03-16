soma = cont = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram inseridos {cont}, a soma total deles foi {soma}')

