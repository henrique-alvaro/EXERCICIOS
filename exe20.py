# pedindo 4 nomes para uma sequencia de apresentaçao
import random
n1 = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n3 = str(input('Aluno 3: '))
n4 = str(input('Aluno 4: '))
# adicionando os nomes em uma lista
lista = [n1, n2, n3, n4]
random.shuffle(lista)
# mostrando a sequencia de apresentaçao
print(f'Lista de Apresentaçao: {lista}')



