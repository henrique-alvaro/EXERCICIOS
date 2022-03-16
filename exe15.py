# sabendo quantos dias voce ficou com carro e quantos km voce andou com carro
dia = int(input('Quantos dias com o carro: '))
km = float(input('Quantos KM andado com carro: '))
# calculando valor das diarias e dos km andado
totaldia = dia * 60
totalkm = km * 0.15
# mostrando valor que tem de ser pago pelas diarias e km andado
print(f'Voce ficou {dia}D com carro, preço da sua diaria ficou: R$:{totaldia}')
print(f'Voce andou {km}km com carro, preço da kilometragen andada ficou: R$:{totalkm}')
print(f'preço Total: R$:{totalkm + totalkm}')
