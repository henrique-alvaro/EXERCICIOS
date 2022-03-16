def aumentar(preço, taxa):
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço, taxa):
    res = (preço * taxa/100)
    return res


def dobro(n):
    dobro = n * 2
    return dobro


def metade(n):
    metade = n / 2
    return metade
