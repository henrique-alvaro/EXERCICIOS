cad = dict()
gols = list()
tot = 0
cad['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {cad["nome"]} jogou: '))
for c in range(partidas):
    g = int(input(f'Quantas gols na {c+1}° partida: '))
    gols.append(g)
    tot += g
cad['gols'] = gols.copy()
cad['total'] = tot
print('-='*20)
print(cad)
print('-='*20)
for k, v in cad.items():
    print(f'{k} tem o valor: {v}')
print('-='*20)
for i, l in enumerate(cad['gols']):
    print(f' => Na partida {i+1} fez {l} gols')