# pedindo um numero 
num = int(input('Digite um numero: '))
cont = 0
# fazendo a analise se os numeros sao primo ou nao
for c in range(1, num+1):
    # inserindo cores verde nos que sao multiplicados pelo numero inserido
    if num % c == 0:
        print('\033[32m',end='')
        cont += 1
    # ou se nao sao multiplicados inserindo o numero vermelho
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
# mostrando numeros que sao e nao sao multiplicados pelo numero inserido
print(f'\n\033[mO numero {c} e divisivel {cont} vezes')
# analisando qual numero e primo é nao e primo
# se o numero inserido for multiplicado apenas duas vezes ele e primo
if cont == 2:
    print('Porisso o numero e PRIMO')
# se for for multiplicado mais de 2 vezes ele nao e primo
else:
    print('Porisso o numero nao e PRIMO')
