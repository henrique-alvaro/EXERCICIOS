totmulher = tothomen = tot18 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tothomen += 1
    if sexo == 'F' and idade < 20:
        totmulher += 1
    d = ' '
    while d not in 'SN':
        d = str(input('Deseja Continuar [S/N]: ')).upper()[0]
    if d == 'N':
        break
print(f'Foram cadastrados {tot18} pessoas maior de 18 anos')
print(f'Foram cadastrados {tothomen} Homens')
print(f'Foram cadastrados {totmulher} mulheres menores de 20 anos')
