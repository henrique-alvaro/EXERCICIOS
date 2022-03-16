notas = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Digite a 1° nota: '))
    n2 = float(input('Digite a 2° nota: '))
    media = (n1 + n2) / 2
    notas.append([nome, [n1, n2], media])
    d = ' '
    while d not in 'SN':
        d = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
    if d in 'N':
        break
print('-='*20)
print(f'{"No.":<4}{"Nome":<10}{"Media":>10}')
print('-='*20)
for i, l in enumerate(notas):
    print(f'{i:<4}{l[0]:<10}{l[2]:>10}')
print('-='*20)
while True:
    aluno = int(input('Notas de qual Anluno deseja ver (999 interrompe): '))
    if aluno == 999:
        break
    if aluno <= len(notas) - 1:
        print(f'Notas de {notas[aluno][0]} sao {notas[aluno][1]}')
    else:
        print('ERRO aluno nao exitente')
print('<<< Programa Encerrado >>>')
    