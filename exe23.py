# pedindo um valor
num = int(input('Digite um numero: '))
# calculando unidade, dezena, centena e milhar do valor
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
mihar = num // 1000 % 10
# mostrando unidades, dezenas, centenas e milhares do valor
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {mihar}')


