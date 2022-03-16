# criando um cadastro de pessoas com nome, idade e sexo
soma = 0
idadedohomenmaisvelho = 0
nomedohomenmaisvelho = ''
totmulher = 0
for c in range(1, 5):
    # pedindo nome
    nome = str(input('Digite um Nome: '))
    # pedindo idade
    idade = int(input('Idade: '))
    # pedindo sexo
    sexo = str(input('Sexo: ')).strip()
    # criando uma somatoria das idades
    soma += idade
    # analisando o nomedo homen mais velho e a idade
    if c == 1 and sexo in 'Mm':
        idadedohomenmaisvelho = idade
        nomedohomenmaisvelho = nome
    if idade > idadedohomenmaisvelho and sexo in 'Mm':
        idadedohomenmaisvelho = idade
        nomedohomenmaisvelho = nome
    # analisando quais mulheres sao menores de 20 anos 
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
    print('-'*20)
# tirando a media de todasa as idades
media = soma / 4
# mostrando a media de idade delas
print(f'A media de idade das pessoas inscritas e: {media}')
# mostrando idade e nomes do homen mais velho
print(f'O homen mais velho tem {idadedohomenmaisvelho} e se chama {nomedohomenmaisvelho}')
# mostrando quantidade de mulheres que tem menos de 20 anos
print(f'O Total mulheres com menos de 20: {totmulher}')
