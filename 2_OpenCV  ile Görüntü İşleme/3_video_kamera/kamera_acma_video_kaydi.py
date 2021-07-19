# -*- coding: utf-8 -*-
"""
Kamera Açma ve Video Kaydı
Kamera açma ve video kaydetmeyi öğreneceğiz.
"""

"""
Bu neden önemli veri toplama açısından önemli.
Çünkü atıyorumki bir nesne tespiti probleminde biz kendi verilerimizi toplayacağız.
Bu nedenle bizim bir kameramız olmalı ki çeşitlilik sağlayabilelim
"""
import cv2

#capture
cap = cv2.VideoCapture(0)
# Buradaki 0, bizim default kameramızdır. Laptop kullanıyorsanız;
# harici bir kamera taktığınız zaman burayı 0 ya da 1 olarak setlemeniz gerekir.
# Sizin atıyorum normal bir bilgisayarınız var masaüstü, 
# ve burada bir kamera, yani laptoptaki gibi bir kameraya sahip değilseniz;
# dışarıdan bir harici kamera taktıysanız buraya 0 yazmak zorundasınuz.
# Ama bilgisayarınızda iki kamera varsa 0 ya da 1 yazmak zorundasınız hangisini kullanmak istiyorsanız.

# videonun genişliği ve yüksekliğine bakalım:
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)

# video kaydedici:
# frameler okundukça ve bizim ekranımızda görselleştirildikçe
# pararlelden de aynı zamanda bu video kaydediciye kaydedilecek
writer = cv2.VideoWriter("video_kaydi.mp4", cv2.VideoWriter_fourcc(*"DIVX"),20,(width, height))
# writer diye bir tane yazıcı değişken oluşturalım.
# CideoWriter_fourcc() bunu windows için kullanıyoruz.
# fourcc dediğimiz şey çerçeveleri sıkıştırmak için kullanılan 4 karakterli codex kodu.
# bunu ne yapacağız şimdi (*"DIVX") bu windows için.
# 20 yapmamız frame por second'ımız(video akış hızı = her saniyede göreceğimiz frame(resim) sayısı) 
# çok önemli değil burayı çok büyük yapamadığınız sürece değiştirebilirsiniz.
# ve ensondada çerçevenin genişlik ve yüksekliği
# bu benim video kaydedicim..

# şimdi video okuyacağız, görselleştireceğiz ve paralelde video kaydı gerçekleştireceğiz..
while True:
    ret, frame = cap.read()
    cv2.imshow("video", frame)
    
    #save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
writer.release()
cv2.destroyAllWindows()
# ilerleyen bölümlerde kendi verimizi tespit edeceğiz o yüzden bu gerekli.