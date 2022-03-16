# pedindo um ano 
ano = int(input('Ano: '))
# analisando se o ano e bissexto ou Nao, para mostrar!
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    
    print(f'O ano {ano} e BISSEXTO')
else:
    print(f'O ano {ano} nao e BISSEXTO')
