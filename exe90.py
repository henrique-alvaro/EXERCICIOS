cadastro = dict()
cadastro['nome'] = str(input('Nome: ')).strip().title()
cadastro['media'] = float(input('Media: '))
print('-='*20)
print(f' - Nome igual a {cadastro["nome"]}')
print(f' - Media igaul a {cadastro["media"]}')
if cadastro['media'] >= 7:
    print(f' - Aluno Aprovado')
elif 5 <= cadastro['media'] < 7:
    print(f' - Aluno de Recuperação')
else:
    print(' - Aluno de Reprovado')
