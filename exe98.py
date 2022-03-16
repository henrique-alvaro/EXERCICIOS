from time import sleep


def lin():
    print('-='*20)


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1        
    lin()
    print(f'Contagem {i} ate {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('Fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('Fim')
        
        
contador(1, 10, 1)
contador(10, 1, 2)
lin()
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
