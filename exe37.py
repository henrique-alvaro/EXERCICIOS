# pedindo un numero 
num = int(input('Escolha um numero: '))
# mostando opções de conversão para o Numero
print('''Escolha um Opçao
[ 1 ] Converter para Binario
[ 2 ] Converter para Octagonal
[ 3 ] Converter para Hexedecimal''')
# escolhendo qual opçao de conversão vai querer
opçao = int(input('Escolha uma Opçao: '))
# fazendo a converção e mostrando o valor convertido
if opçao == 1:
    print(f'{num} convertido para BINARIO e igual a {bin(num)[2:]}')
elif opçao == 2:
    print(f'{num} convertido para OCTAGONAL e igual a {oct(num)[2:]}')
elif opçao == 3:
    print(f'{num} convertido para HEXADECIMAL e igual a {hex(num)[2:]}')
else:
    print('ERRO! opçao invalida')
