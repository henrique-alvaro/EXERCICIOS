# pedindo 2 notas em números real
from time import sleep
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
# calculando a  media do aluno
media = (n1 + n2) / 2
# analisando sé o aluno estar Reprovado, Recuperação ou Aprovado de série
if media < 5:
    print(f'Tirando {n1} e {n2}, a Media do aluno e {media:.2f}')
    sleep(0.5)
    print('ALUNO REPROVADO')
elif 5 < media < 7:
    print(f'Tirando {n1} e {n2}, a media do aluno e {media:.2f}')
    print('ALUNO DE RECUPERAÇAO')
else:
    print(f'Tirando {n1} e {n2}, a media do aluno e {media:.2f}')
    print('ALUNO APROVADO')
