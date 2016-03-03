#######################################################
#                                                     #
#                                                     #
#  Deneme çalışmaları bu dosyada yapılır.             #
#                                                     #
#                                                     #
#######################################################

#from tkinter import *
#from Dosya_islemleri import *

#pencere = Tk()
#pencere.title("Şifreleme Test")
from datetime import date

from gi.overrides.keysyms import End


def geriCevir(x):
    return chr(x)

#def yapistir():

with open("Test.txt", "r") as dosya:
    oku = dosya.read()
    print(oku)

def f(x):
    return ord(x)+5

def coz(x):
    return ord(x)-5

sifre = list(map(coz, oku))
sifrelimetin = ''.join(geriCevir(i) for i in sifre)

with open("Test.txt", "w") as dosya:
    dosya.write(sifrelimetin)
    print(sifrelimetin)

