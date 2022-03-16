# pedindo um numero para calcular fatorial dele
n = int(input('Digite um numero: '))
c = n
f = 1
# mostrando qual fatorial vai ser calculada
print(f'Calculando: {n}! = ', end='')
# calculando a fatorial
while c > 0:
    # decrescendo o numero
    print(f'{c}', end='')
    # numero maior que 1 inseri o x, e numero menor que 1 inseri = 
    print(' x ' if c > 1 else ' = ', end='')
    # multiplicando os numeros com sua decresenza
    f *= c
    # decrescento o numero todoa vez no laço até chegar no 1
    c -= 1
print(f)
