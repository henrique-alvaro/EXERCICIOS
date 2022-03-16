# Criando um numero para mostrar a tabuada
num = int(input('Digite um numero para ver sua tabuada:'))
# gerando a tabuada
for c in range(1, 11, 1):
    print(f'{num} x {c:2} = {c*num}')