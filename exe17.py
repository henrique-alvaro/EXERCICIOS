# pedindo um cateto oposto e um cateto adjacente
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
# calculando os cateto para encontrar um hipotenusa
hi = (co ** 2 + ca ** 2) / 0.5
# mostrando a hipotenusa dos catetos
print(f'Cateto oposto: {co}, cateto Adjacente {ca}')
print(f'Hipotenusa: {hi}')
