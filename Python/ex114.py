# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessivel no momento')
else:
    print('Deu certo')