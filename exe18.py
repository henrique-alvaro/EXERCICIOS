# pedindo seno, cosseno e tangente
import math
angulo = float(input('Angulo: '))
# calculando seno, cosseno e tangente com a biblioteca math
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
# mostrando resultado de seno, cosseno e tangente
print(f'Seu angulo e {angulo}')
print(f'Seno do angulo e {sen:.2f}')
print(f'Cosseno do angulo e {cos:.2f}')
print(f'Tangente do angulo e {tan:.2f}')
