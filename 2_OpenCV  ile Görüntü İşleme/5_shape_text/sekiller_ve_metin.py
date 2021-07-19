"""
Şekiller ve Metin

Şekillerin örneğin çizgi, daire, diktörtgen gibi resim üzerine nasıl eklendiğini göreceğiz.
Metinlerin resim üzerine nasıl eklendiğini göreceğiz.
"""

import cv2
import numpy as np
# ayrıca birde numpy kütüphanesini ekliyoruz.
# çünkü neden bu sefer bir resim üretmek veya yüklemek yerine
# nump kütüphanesini kullarak siyah bir tane resim oluşturacağım

img  = np.zeros((512,512,3), np.uint8) #siyah bir resim
# siyah 0 a yaklaştığımızda gördüğümüz değerdir.
print(img.shape)
cv2.imshow("Siyah", img)

# çizgi
cv2.line(img, (100,100), (100,300),(0,255,0),3)
cv2.imshow("Cizgi", img) 
# resmimiz, başlangıç nok., bitiş nok., renk, çizginin kalınlığı
# RGB (0,0,255) -> kırmızı (255,0,0) -> mavi (0,255,0)-> yeşil
# OpenCV bunu RGB yerine BGR(blue, green, red) olarak kabul ediyor.

# dikdörtgen
# resim, baş nok., bitis nok,renk
cv2.rectangle(img, ( 0,0), (256,256), (255,0,0),cv2.FILLED)
cv2.imshow("Dikdortgen", img)
# Dikdörtgenin içini doldurmak için FILLED

# çember
# resim, merkez, yarıçapı, renk
cv2.circle(img, (300,300), 45, (0,0,255), cv2.FILLED)
cv2.imshow("Cember", img)

#metin ekleme
# resim, yazı baş.nok., font, yazı kalınlığı, renk
cv2.putText(img, "Resim", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("Metin", img)