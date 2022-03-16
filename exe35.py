# pedindo 3 retas 
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
# analisando se as retas forman um triangulo ou nao,
# logo em seguinda deve mostrar se forman ou nao um triangulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As Reatas podem formar um triangulo')
else:
    print('As Retas nao podem forma um triangulo')
