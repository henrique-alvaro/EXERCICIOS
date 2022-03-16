# pedindo um nome
nome = str(input('Nome completo: ')).strip()
# colocando todo o nome em maiusculo
print(f'Nome todo em maiusculo: {nome.upper()}')
# colocando todo o nome em minusculo
print(f'Nome todo em minusculo: {nome.lower()}')
# sabendo o total de letras tem todo o nome
print(f'Total de letras tem o nome: {len(nome)-nome.count(" ")}')
# sabendo quantas letras tem o primeiro nome
separa = nome.split()
# mostrando total de letras tem o primeiro nome
print(f'Seu primeiro nome e {separa[0]} tem {len(separa[0])} letras')
