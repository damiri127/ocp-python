from pemukul import Pemukul
from penabrak import Penabrak
from penembak import Penembak

karakter1 = Penembak("Asep", 30)
print(karakter1.menyerang(),",menembak")

karakter2 = Pemukul("Malik", 50)
print(karakter2.menyerang(),",memukul")

karakter3 = Penabrak("Fatur", 80)
print(karakter3.menyerang(), ",menabrak")