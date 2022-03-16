cont = 0
while True:
    num = int(input('Digite numero para tabuada: '))
    for c in range(1, 11):
        print(f'{num} x {c:2} = {c*num}')
    d = ''
    while True:
        d = str(input('Deseja Continuar [S/N]: ')).upper()[0]
        if d in 'SN':
            break
        print('ERRO digite apenas S ou N')
    if d in 'N':
        break
print('Programa Encerrado')
    