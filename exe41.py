# pedindo um ano de nascimento para ser analisado
from datetime import datetime
print('<<< ANALISANDO IDADE PARA ALISTAMENTO >>>')
ano = int(input('Ano: '))
print('--'*20)
# sabendo o ano atual
new = datetime.now().year
# calculando a idade com ano de nascimento e ano atual
idade = new - ano
# analisando idade para alistamento militar
# verificando se falta ou ja passou do tempo para se alistar
# ou se estiver na hora avisar para ele ir se alistar
if 0 < idade <= 9:
    print('MIRIN')
elif 9 < idade <= 14:
    print('INFATIL')
elif 14 < idade <= 19:
    print('JÚNIOR')
elif 19 < idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
print('--'*20)
