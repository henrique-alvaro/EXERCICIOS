# pedindo 3 numeros inteiros
n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))
# analisando qual dos 3 e o maior e menor
menor = 0
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n1:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n1:
    maior = n3
# mostrando o numero maior e o maior
print(f'O maior numero e: {maior}')
print(f'O maior numero e: {menor}')
