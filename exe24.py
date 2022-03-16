# perguntando se sua cidade começa com SANTO
cid = str(input('Sua cidade começa com (SANTO): ')).strip()
# analisando se a cidade começa ou nao com SANTO
print(cid[:5].upper() == 'SANTO')
