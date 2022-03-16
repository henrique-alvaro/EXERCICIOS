from exe115.lib.interface import *
from exe115.lib.arquivo import *

arq = 'arquivocursoemvideot.txt'

if not arquivoExiste(arq):
    criararquivo(arq)


cabeçalho('SISTEMA ARQUIVO v1.0')
while True:
    p = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Programa'])
    if p == 1:
        # ler arquivo para cadastro de pessoas
        lerarquivo(arq)
    elif p == 2:
        cabeçalho('Opçao 2')
    elif p == 4:
        cabeçalho('Saindo do Programa')
        break
    else:
        cabeçalho('Opçao invalida')
