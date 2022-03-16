# criando um medidor de velocidade
from time import sleep
# perguntando a velocidade do carro
vel = float(input('Qual e a velocidade: '))
sleep(1)
# analisando se estar acima ou nao da velocidade para aplicar a multa
if vel > 80:
    print(f'Sua velocidade e {vel}km/h')
    sleep(0.5)
    acima = vel - 80
    print(f'Voce Ficou {acima}km/h acima da velocidade permitida')
    print(f'Sua multa e de R$:{acima*7}')
else:
    print(f'Sua velocidade e {vel}km/h')
    sleep(0.5)
    print('Bom dia, digija com cuidado!')
