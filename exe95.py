dados = dict()
lista = list()
gols = list()
tot = 0
while True:
    dados.clear()
    gols.clear()
    dados['nome'] = str(input('Nome: ')).title()
    partidas = int(input(f'Quantas Partidas {dados["nome"]} jogou: '))
    for c in range(partidas):
        g = int(input(f'Quatos gols na {c+1}° partida: '))
        gols.append(g)
    dados['gols'] = gols.copy()
    dados['total'] = sum(gols)
    lista.append(dados.copy())
    while True:
        pergunta = str(input('Deseja Continuar [S/N]:')).upper()[0]
        if pergunta in 'SN':
            break
    if pergunta == 'N':
        break
print('-='*20)
print('cod ', end='')
for c in dados.keys():
    print(f'{c:<15}', end='')
print()
print('-='*20)
for k, v in enumerate(lista):
    print(f'{k:>2}  ', end='')
    for i in v.values():
        print(f'{str(i):<15}', end='')
    print()
print('-='*20)
while True:
    busca = int(input('Mostar dados de qual jogador (999 interrompe): '))
    if busca == 999:
        break
    if busca >= len(lista):
        print('ERRO jogador nao existe')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {lista[busca]["nome"]} ---')
        for i, g in enumerate(lista[busca]['gols']):
            print(f'   No jogo {i} fez {g} gols')
        