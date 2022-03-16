def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gols(s) na partida')


nome = str(input('Nome do Jogador: '))
gols = str(input('Gols do Jogador: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
