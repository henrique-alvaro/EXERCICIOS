# pedindo 2 numeros
n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
# analisando qual numero e maior, menor ou sé são iguais
if n1 > n2:
    print('Primeiro valor e Maior')
elif n2 > n1:
    print('Segundo valor e Maior')
else:
    print('Nao tem valor maior. Os dois sao iguais')
