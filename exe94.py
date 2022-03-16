cad = dict()
lista = list()
soma = media = 0
while True:
    cad.clear()
    cad['nome'] = str(input('Nome: ')).title()
    while True:
        cad['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if cad['sexo'] in 'MF':
            break
        print('ERRO digite apenas M ou F.')
    cad['idade'] = int(input('Idade: '))
    soma += cad['idade']
    lista.append(cad.copy())
    while True:
        d = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
        if d in 'SN':
            break
    if d == 'N':
        break
print('-='*20)
print(f'A) -> Foram cadastradas {len(lista)} pessoas')
media = soma / len(lista)
print(f'B) -> A media de idade das pessoas cadastradas e: {media}')
print(f'C) -> As mulheres cadastrasdas foi: ', end='')
for m in lista:
    if m['sexo'] in 'Ff':
        print(f'{m["nome"]} ', end='')
print()
print('D) -> Pessoas acima da media de idade:')
for m in lista:
    if m['idade'] >= media:
        print(' => ', end='')
        for k, v in m.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< PROGRAMA ENCERRADO >>>')
