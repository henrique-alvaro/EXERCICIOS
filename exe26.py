# pedindo um frase
frase = str(input('Digite um frase: ')).strip().upper()
# analisando quantas letras tem A tem na frase
print(f'A letra A aparece {frase.count("A")} vezes na frase')
# analisando onde aparece a 1° letra A
print(f'A 1° letra A aparece na {frase.find("A")+1}° posiçao')
# analisando em qual posiçao a ultima letra A aparece
print(f'A ultima letra A aparece na {frase.rfind("A")+1}° posiçao ')

