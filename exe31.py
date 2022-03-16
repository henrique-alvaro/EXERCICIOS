# pedindo uma distancia de viaje
distancia = float(input('Distancia da viaje: '))
# calculando a distancia da viaje se e maior de 200km ou menor
if distancia > 200:
    valor = distancia * 0.45
    # mostrando o vlaor da viaje caso seja maior de 200km
    print('Voce entrou na nossa promoçao')
    print(f'Valor da viagem e de: R$:{valor}')
    print('Boa viagem')
else:
    valor = distancia * 0.50
    # mostrando o valor da viagem caso seja menor de 200km
    print(f'Valor da sua passagem e de: R$:{valor}')
    print('Boa Viagem')