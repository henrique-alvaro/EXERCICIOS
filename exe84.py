reserva = list()
principal = list()
maior = menor = 0
while True:
    reserva.append(str(input('Nome: ')))
    reserva.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = reserva[1]
    else:
        if reserva[1] > maior:
            maior = reserva[1]
        if reserva[1] < menor:
            menor = reserva[1]
    principal.append(reserva[:])
    reserva.clear()
    d = ' '
    while d not in 'SN':
        d = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
    if d == 'N':
        break
print('-='*20)
print(f'Ao todo {len(principal)} pessoas foram inscrito')
print(f'O maior peso foi {maior}. Peso de ', end='')
for c in principal:
    if c[1] == maior:
        print(f'{c[0]}' , end='')
print()
print(f'O menor peso foi {menor}. Peso de ', end='')
for c in principal:
    if c[1] == menor:
        print(f'{c[0]}' , end='')
print()
