# pedindo uma frase aleatoria
digite = str(input('Digite Algo: '))
# qual tipo primitivo da frase
print('Seu tipo primitivo e:', type(digite))
# se a frase e composta so de espaços
print('So tem espaços: ', digite.isspace())
# se a frase e somente e somente numerico
print('E numerico: ', digite.isnumeric())
# se a frase e somente alfabetica
print('E alfabetico: ', digite.isalpha())
# se a frase e composta por letra e numero
print('E Alfanumerico: ', digite.isalnum())
# se a frase e composta somente por letra maiuscula
print('Esta em maiusculo: ', digite.isupper())
# se a frase e composta somente por letra minuscula
print('Esta em minusculo: ', digite.islower())
# se a frase e capitalizada
print('Esta caitalizado: ', digite.istitle())

