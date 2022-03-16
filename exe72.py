extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quartoze', 'Quinze',
           'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um numero: '))
    if 0 <= num <= 20:
        break
    print('ERRO digite novamente')
print(f'Seu numero e {num} por extenso fica {extenso[num]}')
