def aumentar(preço, taxa, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    dobro = preço * 2
    return dobro if formato is False else moeda(dobro)


def metade(preço=0, formato=False):
    metade = preço / 2
    return metade if formato is False else moeda(metade)


def moeda(preço, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(preço)}')
    print(f'Dobro do Preço: \t{dobro(preço, True)}')
    print(f'Metade do Preço: \t{metade(preço, True)}')
    print(f'{taxaa}% aumento: \t\t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% diminuindo: \t\t{diminuir(preço, taxar, True)}')
    print('-' * 30)
