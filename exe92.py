from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - ano
dados['ctps'] = int(input('Ctps: '))
if dados['ctps'] != 0:
    dados['contrataçao'] = int(input('Contrataçao: '))
    dados['salario'] = float(input('Salario: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contrataçao'] + 35) - datetime.now().year)
print('-='*20)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
