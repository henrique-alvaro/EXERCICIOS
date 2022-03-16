from time import sleep
def ajuda(com):
    titulo(f'\033[0;30;44mAcessando o manual do comando \'{com}\'\033[m')
    print('\033[0;30;107m', end='')
    help(com)
    print('\033[m', end='')
    sleep(2)

def titulo(msg):
    tam = len(msg) + 4
    print('\033[0;30;42', end='')
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print('\033[m', end='')


comando = ''
while True:
    titulo('\033[0;30;42mSISTEMA DE AJUDA PyHELP\033[m')
    comando = str(input('Funçao ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('\033[0;30;41mATÉ LOGO!\033[m')
