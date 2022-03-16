# pedindo 4 nomes para dentre eles um ser sorteado 1
import random
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
# adicinando os nomes em uma lista
lista = [a1, a2, a3, a4]
# sorteando um nome
print(f'Sorteando um aluno: {random.choice(lista)}')

