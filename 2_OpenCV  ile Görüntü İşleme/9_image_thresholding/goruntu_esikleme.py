"""
Görüntü Eşikleme
Bu bölümde eşik değerlerinin resimler üzerinde etkisini göreceğiz.
"""

import cv2
import matplotlib.pyplot as plt

#resmi içe aktar
img = cv2.imread("img1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(img, cmap  = "gray")
plt.axis("off")
plt.show()

# threshold (eşikleme)

"""
threshold methodu iki tane şeyi return ediyor.
Bir tanesi bizim için önemli değil bu yüzden alt çizgi "_" kullanıyoruz.
thres_img yani threshold u alınmış img
resmimize uygulayacağız threshold'un bir alt sınırı var biz bunu 60 olarak seçeceğiz.'
yani bu threshol üzerindeki değerleri görmek istemiyorum bunları beyaz yapacağız.
ve maxval maximum değerim 255ti .
ve threshold type ise thresh_bınary eşik türünü kullanmamızın sebebi :
eşik değerlerinde kullanılacak maximum ve minimum değerlerin arasında açıyor ya da kapatıyor

"""

_, thresh_img = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY)

plt.figure()
plt.imshow(thresh_img, cmap  = "gray")
plt.axis("off")
plt.show()

# uyarlamalı eşik değeri
"""
ADAPTIVE_THRESH_MEAN_C dediğimiz şey bizim adaptive methodumuz. 
Buradaki c sayısı 8 bizim c sayısımız oluyor ve c sabiti ortalamadan veya ağırlık ortalamadan
çıkarılabilecek bir değer. normalde pozitif ama 0 veya negatif yapılabiliyor.

Buradaki c sabitine göre bir ortalama alınıyor.
ve bu bizim kullanacağımız threshold değeri oluyor.

"""

thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,8)

plt.figure()
plt.imshow(thresh_img2, cmap  = "gray")
plt.axis("off")
plt.show()
