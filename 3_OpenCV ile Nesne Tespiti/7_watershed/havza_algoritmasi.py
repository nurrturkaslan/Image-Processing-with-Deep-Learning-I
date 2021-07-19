"""
Havza Algoritması:
    Havza, segmentasyon için, yani bir görüntüdeki farklı nesneleri ayırmak için kullanılan klasik bir algoritmadır


1- Herhangi gri tonlamalı görüntü, yüksek yoğunluğun zirveleri ve
tepeleri, düşük yoğunluğun vadileri ifade ettiği topografik yüzey olarak görülebilir.

2-İzole edilmiş her vadiyi(yerel minimum) farklı renkli suyla (etiketler)
doldurmaya başlarsınız.

3- Su yükseldikçe, yakınlardaki zirvelere(gradyanlara) bağlı olarak, farklı vadilerden gelen su belli ki farklı renklerle birleşmeye başlayacaktır

4-Bundan kaçınmak için suyun birleştiği yerlere bariyerler inşa edersiniz. Tüm zirveler su altında kalana kadar su doldurma ve bariyerler
inşa etme işine devam ediyorsunuz.

5-Daha sonra oluşturduğunuz engeller size segmentasyon sonucunu verir.

"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

# resmi içe aktar
coin = cv2.imread("coins.jpg")
plt.figure()
plt.imshow(coin)
plt.axis("off")

# resim üzerinde bulunan şekillerden kurtulmak için
#lpf: blurring
coin_blur = cv2.medianBlur(coin, 13)
plt.figure()
plt.imshow(coin_blur)
plt.axis("off")

#renki resmi siyah beyaz yap
coin_gray = cv2.cvtColor(coin_blur, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(coin_gray, cmap = "gray")
plt.axis("off")

# binary threshold
# vadi ile tepeler arasındaki varkı BİNARY THRESHOLD ile daha çok açacağız.
ret, coin_thresh = cv2.threshold(coin_gray, 75, 255, cv2.THRESH_BINARY)
plt.figure()
plt.imshow(coin_thresh, cmap = "gray")
plt.axis("off")


#kontur
#_, contours, hierarchy = cv2.findContours(coin_thresh.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv2.findContours(coin_thresh.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(coin, contours, i, (0,255,0), 10)
plt.figure()
plt.imshow(coin, cmap = "gray")
plt.axis("off")       

#watershed
coin = cv2.imread("coins.jpg")
plt.figure()
plt.imshow(coin)
plt.axis("off")


coin_blur = cv2.medianBlur(coin, 13)
plt.figure()
plt.imshow(coin_blur)
plt.axis("off")

coin_gray = cv2.cvtColor(coin_blur, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(coin_gray, cmap = "gray")
plt.axis("off")


ret, coin_thresh = cv2.threshold(coin_gray, 65, 255, cv2.THRESH_BINARY)
plt.figure()
plt.imshow(coin_thresh, cmap = "gray")
plt.axis("off")

#nesnelerin arası olusan köprüleri engellemek için
#nesnelerin boyutunu küçültürsek nesneler birbirinden ayrılır

#açılma
#açılma dediğimiz için erozyon ve genişlemeydi

kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(coin_thresh, cv2.MORPH_OPEN, kernel, iterations = 2)
plt.figure(), plt.imshow(opening, cmap="gray"), plt.axis("off")

# nesneler arası distance bulalım
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
plt.figure(), plt.imshow(dist_transform, cmap="gray"), plt.axis("off")

# resmi küçült
ret, sure_foreground = cv2.threshold(dist_transform, 0.4*np.max(dist_transform),255,0)
plt.figure(), plt.imshow(sure_foreground, cmap="gray"), plt.axis("off")

# arka plan için resmi büyült
sure_background = cv2.dilate(opening, kernel, iterations = 1)
sure_foreground = np.uint8(sure_foreground)
unknown = cv2.subtract(sure_background,sure_foreground)
plt.figure(), plt.imshow(unknown, cmap="gray"), plt.axis("off")

# bağlantı
ret, marker = cv2.connectedComponents(sure_foreground)
marker = marker + 1
marker[unknown == 255] = 0
plt.figure(), plt.imshow(marker, cmap="gray"), plt.axis("off")

# havza
marker = cv2.watershed(coin,marker)
plt.figure(), plt.imshow(marker, cmap="gray"), plt.axis("off")


# kontur
# _, contours, hierarchy = cv2.findContours(coin_thresh.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv2.findContours(marker.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(coin, contours,i,(255,0,0),2)
plt.figure(),plt.imshow(coin),plt.axis("off")


















