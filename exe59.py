# pedindo 2 numeros
num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))
opçao = 0
# criando uma lista de opções calcular 2 valores inseridos
# enquanto opção for diferente de 5 o laço continua porque so tem 4 opções
while opçao != 5:
    # mostrando opções
    print(''' Escolha sua Opção
    [ 1 ] Somar
    [ 2 ] Multilicar
    [ 3 ] Maior
    [ 4 ] Novos Numeros
    [ 5 ] Sair do Programa''')
    # escolhendo opções para calcular os 2 valores
    opçao = int(input('Escolha sua Opção: '))
    # se for 1° opção entao vai somar os 2 valores
    if opçao == 1:
        soma = num1 + num2
        print(f'A soma dos {num1} + {num2} = {soma}')
    # se for 2 entao vai multiplicar os 2 valores
    elif opçao == 2:
        multiplicaçao = num1 * num2
        print(f'A Multilicar dos {num1} x {num2} = {multiplicaçao}')
    # se for 3 entao vai mostrar o maior numero
    elif opçao == 3:
        maior = 0
        manor = 0
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'O Maior numero e: {maior}')
    # se for 4 vai pedir novos numeros
    elif opçao == 4:
        print('Digite novos Numeros')
        num1 = int(input('Numero 1: '))
        num2 = int(input('Numero 2: '))
    # se for 5 vai sair do programa
    elif opçao == 5:
        break
    # agora se for diferante de 5 vai da erro
    else:
        print('Opção Invalida')
print('Programa Encerrado')