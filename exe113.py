def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mERRO! digite um valor inteiro valido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO Usuario preferiu digitar nenhum valor\033[m')
            continue
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mERRO! digite um valor Real valido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO Usuario preferiu digitar nenhum valor\033[m')
        else:
            return n


n1 = leiaint('Digite valor inteiro: ')
n2 = leiafloat('Digite um valor Real: ')
print(f'O valor inteiro digitado foi {n1} e o valor real digitado foi {n2}')

