times = ('atletico-mg', 'flamengo', 'palmeiras', 'fortaleza', 'corinthias',
         'bragantino', 'fluminense', 'america-mg', 'atletico-go', 'santos',
         'ceara', 'international', 'sao paulo', 'athletico-pr', 'cuiba',
         'juventude', 'gremio', 'bahia', 'sport', 'chapecoense')
print('-='*35)
print('LISta de times do BRASILEIRAO SERIE "A"')
print('-='*35)
print(f'Oo primeiros 5 colocados {times[:5]}')
print('-='*35)
print(f'Os 4 ultimos colocados sao {times[-4:]}')
print('-='*35)
print(f'Todos os times por ordem alfabetica {sorted(times)}')
print('-='*35)
print(f'Chapecoense estar em {times.index("chapecoense")+1}° lugar')
print('-='*35)
