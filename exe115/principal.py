from exe115.lib.interface import *
from exe115.lib.arquivo import *

arq = 'arquivocursoemvideot.txt'

if not arquivoExiste(arq):
    criararquivo(arq)


cabeçalho('SISTEMA ARQUIVO v1.0')
while True:
    p = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Programa'])
    if p == 1:
        # ler arquivo para cadastro de pessoas
        lerarquivo(arq)
    elif p == 2:
        # Cadastrando nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastro(arq, nome, idade)
    elif p == 3:
        cabeçalho('Saindo do Programa')
        break
    else:
        print('Opçao invalida')
