# criando um cadastro de sexo
while True:
    # pedindo se o sexo é Masculino ou Feminina
    sexo = str(input('Qual e o seu Sexo [M/F]: ')).strip().upper()
    # analisando foi inserido o sexo da pessoa certo nao
    if sexo in 'MmFf':
        break
    print('Dados invalido, digite novamnete')
# mastrando o sexo da pessoa cadastrado
print(f'O Sexo {sexo} foi inscrito com sucesso')
