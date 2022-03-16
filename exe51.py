# pedindo o primeiro termo
primeiro = int(input('Primero Termo: '))
# pedindo uma razao
razao = int(input('Razao: '))
# gerando o calculo do decimo termo da PA
decimo = primeiro + (10 - 1) * razao
# fazendo o termo
for c in range(primeiro, decimo + razao, razao):
    print(c, end=' => ')
print('FIm')