# pedindo uma data de nascimento
from datetime import datetime
ano = int(input('Ano de nascimento: '))
# fazendo o codigo para a data atual
new = datetime.now().year
# calculando a idade com a data de nascimento e data atual para saber a idade
idade = new - ano
# analisando se falta, estar na hora ou ja passou do tempo de ele se alistar no quartel
if idade < 18:
    print(f'voce tem {idade} anos, falta {18-idade} anos para voce se alistar')
elif idade == 18:
    print(f'Voce tem {idade} anos, estar na hora de fazer seu alistamento')
else:
    print(f'Voce tem {idade} anos, passou da hora de voce se alistar')
