import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site nao está acessivel no momento')
else:
    print('Conseguir acessar o site com Sucesso')
