"""
Video İçe Aktarma
Videouyu okumayı, video boyutunu ayarlamayı ve video göstermeyi öğreneceğiz
"""

import cv2
import time

# video ismi
video_name = "MOT17-04-DPM.mp4"

# video içe aktar: capture diye geçer keyword'u capture' dir.
# ve genelde bu cap olarak kısaltılır.

cap = cv2.VideoCapture(video_name) #bu bir obje bunnu göremeyiz ama console'a gelip cap yazarsak videoCapture içerisine aktarıldığını görebiliriz.

# videonun genişlik ve yüksekliği:
print("Genişlik: ", cap.get(3)) # get fonk. 3.indexini uyguladığımda
print("Yükseklik: ", cap.get(4))# 4.indexinde ise yükseklik bulunmakta
# 1920 geniliğinde ,1080 yüksekliğinde yani;
# 1920'ye 1080 piksellerden oluşan bir videomuz var.

# video kontrolü açılıp açılmadığına bakacağız:
if cap.isOpened() == False:
    print("Hata") # şu an öyle bir hata yok video import işlemi tamamdır.
    
# videoyu okumak:
# read methodu bize iki tane şey dönüyor: 1. si return, 2. ise frame.
# frame dediğimiz şey videonun içerisinde bulunan her bir resim her bir frame
# return dediği şeyde bu işlemin başarılı olup olamadığı..
# eğer cap.read işlemi başarısız olduysa; bu bana return false dönecek

while True:
    ret, frame = cap.read()

    if ret == True:
        time.sleep(0.01) #uyarı: kullanmazsak çok hızlı akar.
    
        cv2.imshow("video", frame) # resimleri görselleştirme kodu
    else: break #bu break while döngüsünü kırıyor ve işlemi bitiriyor.
    
    #ama tüm videoyu izlemek istemezsek;
    
    if cv2.waitKey(1) &0xFF  == ord("q"):
        #süresi 1 ve q tuşuna eşitse yani çıkma tuşu
        break
    
cap.release() #video yakalamayı bırak(stop capture)

cv2.destroyAllWindows() #sonrasında tüm açık pencereleri destroy(kapat) et