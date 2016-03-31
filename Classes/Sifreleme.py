#######################################################
#                                                     #
#                                                     #
#                     ŞİFRELEME                       #
#                                                     #
#                                                     #
#######################################################

#from Dosya_islemleri import *

def geriCevir(x):
    return chr(x)

def f(x):
    return ord(x)+5

def coz(x):
    return ord(x)-5

#Şifreleme
with open("Test.txt", "r") as dosya:
    oku = dosya.read()
    print(oku)

sifre = list(map(f, oku))
sifrelimetin = ''.join(geriCevir(i) for i in sifre)

with open("Test.txt", "w") as dosya:
    dosya.write(sifrelimetin)
    print(sifrelimetin)

#################################################################################

#Şifre Çözme
with open("Test.txt", "r") as dosya:
    oku = dosya.read()
    print(oku)

sifre = list(map(coz, oku))
sifrelimetin = ''.join(geriCevir(i) for i in sifre)

with open("Test.txt", "w") as dosya:
    dosya.write(sifrelimetin)
    print(sifrelimetin)
