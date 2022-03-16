def leiaint(msg):
    valor = 0
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um numero\033[m')
        if ok:
            break
    return valor


leiaint('Digite um Numero: ')

