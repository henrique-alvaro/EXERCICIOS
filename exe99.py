from time import sleep

def lin():
    print('--'*20)


def maior(*num):
    lin()
    print('Analisando numeros')
    cont = maior = 0
    for valor in num:
        print(f'{valor} ', end='', flush=True) 
        sleep(0.3)   
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valor ao total')
    print(f'O maior valor informado foi: {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
    