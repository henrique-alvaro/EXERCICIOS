# pedindo um nome completo
nome = str(input('Digite um nome: '))
# separando o nome completo
palavras = nome.split()
# juntando o nome completo sem espaços entre eles
junto = ''.join(palavras)
inverso = ''
# colocando o nome de tras para frente letra por letra
for letra in range(len(junto)-1, -1, -1):
    # somando letra por letra 
    inverso += junto[letra]
# mostrando tanto completo sem espaços, quanto o nome de tras para frente sem espaços
print(f'Nome: {nome} inverso do nome: {inverso}')
# se os dois nomes for identicos entao ele e palindromo
# ou sé nao for identicos nao e palindromo
if inverso == junto:
    print('E PALINDROMO')
else:
    print('NAO E PALINDROMO')
    
