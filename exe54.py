# analisando maioridade
from datetime import datetime
maior = menor = 0
for c in range(1, 8):
    # pedido ano de nascimento 
    ano = int(input('Ano de Nascimento: '))
    # gerando ano atual
    idade = datetime.now().year - ano
    # analisando se a idade e menor ou maior de 18 anos
    if idade >= 18:
        maior += 1
    else:
        menor += 1
# mostrando a quantidade de pessoas maior e menor de idade
print(f'Tem {maior} Pessoas maior de idade, é tem {menor} Pessoas menor de idade')
