def notas(*n, sit=False):
    """
    -> funçao para analisar notas e situações
    param n: uma ou mais notas de alunos (aceita varias)
    param r: um valor opcional se deve ou nao mostrar a situação
    return: dicionario com varias informações sobre os alunos.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['condiçao'] = '\033[32mBoa'
        elif r['media'] >= 5:
            r['condiçao'] = '\033[33mRazoavel'
        else:
            r['condiçao'] = '\033[31mRuim'
    return r


resp = notas(4.4, 5.5, 6, 8.7, sit=True)
print(resp)
#help(notas)
