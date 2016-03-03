#######################################################
#                                                     #
#                                                     #
#                DOSYA İŞLEMLERİ v.1                  #
#                                                     #
#                                                     #
#######################################################

class Dosya_islemleri:

    def Olustur(dosya):
        dosya = open("Test.txt","w")

    def Yaz(dosya):
        with open("Test.txt","w") as dosya:
            dosya.write("Muhammed Nur")

    def Oku(dosya):
        with open("Test.txt", "r") as dosya:
            print(dosya.read())