palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for l in palavras:
    print(f'\nNa palavra {l.upper()} temos: ', end='')
    for letra in l:
        if letra in 'aeiou':
            print(letra, end=' ')