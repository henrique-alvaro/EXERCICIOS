def aumentar(preço, taxa, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    dobro = preço * 2
    return dobro if formato is False else moeda(dobro)


def metade(preço=0, formato=False):
    metade = preço / 2
    return metade if formato is False else moeda(metade)


def moeda(preço, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

