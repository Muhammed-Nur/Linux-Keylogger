#######################################################
#                                                     #
#                                                     #
#                   DOSYA İŞLEMLERİ                   #
#                                                     #
#                                                     #
#######################################################

class Dosya_islemleri:

    def mail(dosya):
        dosya = open("Test.txt","rb")

    def Yaz(dosya):
        with open("Test.txt","w") as dosya:
            dosya.write("Muhammed Nur")

    def Guncelle(dosya):
        global upd
        with open("Test.txt","a") as dosya:
            dosya.write(upd)

    def Oku(dosya):
        with open("Test.txt", "r") as dosya:
            print(dosya.read())
