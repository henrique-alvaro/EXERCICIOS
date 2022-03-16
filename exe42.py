# pedindo 3 retas
from time import sleep
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
print('Analisando')
sleep(1)
# analisando se as retas forman certos triangulo como equilatero, isosceles ou escaleno
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('As Retas forman um triangulo EQUILATERO')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print('As Retas forman um triangulo ISÓSCELES')
    elif r1 != r2 != r3:
        print('As Retas forman um triangulo ESCALENO')
else:
    print('As retas nao forman um triangulo')
