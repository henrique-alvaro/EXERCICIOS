# pedindo um nome completo
nome = str(input('Digite seu nome: ')).strip().title()
# separando o nome
s = nome.split()
# mostrando qual e o primeiro nome
print(f'Seu 1° nome e: {s[0]}')
# mostrando qual e o ultimo nome
print(f'Seu ultimo nome e: {s[-1]}')
