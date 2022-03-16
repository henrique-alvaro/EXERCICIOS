from re import L


ex = str(input('Digite sua Expresao: '))
lista = list()
for simb in lista:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print('Sua expresão estar válida!')
else:
    print('Sua expresão nao estar válida!')