# pedindo a largura de parede
larg = float(input('Largura: '))
# pedindo a altura da parede
alt = float(input('Altura: '))
# calculando a area da parede
area = (larg * alt)
# calculando o tanto de tinta que vai precisar
tinta = area / 2
# mostrando a area que a parede tem
print(f'Sua parede tem medida de {larg}x{alt} com area de {area:.2f}')
# mostrand o tanto de tinta que vai precisar
print(f'Nessecitara de {tinta:.2f}l de tinta para para pintar a parede.')
