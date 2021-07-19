"""
Histogram:
    Görüntü histogramı, dijital görüntüdeki ton dağılımının grafiksel bir temsili olarak işlev gören bir histogram türüdür.
    Her bir ton değeri için piksel sayısını içerir.
    Belirli bir görüntü için histograma bakılarak, ton dağılımı anlaşılabilir.
    
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("red_blue.jpg")
img_vis = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img_vis)

#kaç tane piksel var ona bakalım:
print(img.shape)

#histogramımızı çizdirelim
img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
print(img_hist.shape)
plt.figure()
plt.plot(img_hist)

color = ("b","g","r")
plt.figure()
for i, c in enumerate(color):
    histogram = cv2.calcHist([img], channels = [i], mask = None, histSize = [256], ranges = [0,256])
    plt.plot(histogram, color = c)
    #enumerate dediğimiz şey bu color'u alıyor. içerisinde dönüyor ama çıktı olarak hem b nin indexini i'ye eşitliyor. hem de string olarak b'yi c ye eşitliyor
    #yani color un indexini ve color un tuple ın içerisindeki elemanı return ediyor
#calHist : histogramı hesaplatıyoruz
#channels: RGB mi olduğu yoksa gray scale mi olduğu 0 dediğimizde gray scale anlamında tek bir channel kullanacağım diyorum.
#herhangi bir maskeleme işlemi yapmayacağımız için mask = None
#Maskeleme işlemi resmin belli bir kısmını almakla ilgili


img2 = cv2.imread("goldenGate.jpg")
img2_vis = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img2_vis)

#kaç tane piksel var ona bakalım:
print(img2.shape)

#şimdi buna bir maske oluşturalım. çünkü bu resmin boyutu çok büyük
import numpy as np
mask = np.zeros(img2.shape[:2], np.uint8)
plt.figure()
plt.imshow(mask, cmap = "gray")

#şimdi maskemizi oluşturduk bu maskeyi uygulamakla devam edelim.
#maske içerisinde bir delika açacağız.
#maskeyi resme uyguladıktan sonra deliğin geldiği kısım harici maskelenmiş olacak

mask[1500:2000, 1000:2000] = 255 #255 dediğimizde beyaz oluyor
plt.figure()
plt.imshow(mask, cmap = "gray")

masked_img_vis = cv2.bitwise_and(img2_vis, img2_vis, mask = mask)
plt.figure()
plt.imshow(masked_img_vis, cmap = "gray")

masked_img = cv2.bitwise_and(img2, img2, mask = mask)
masked_img_hist = cv2.calcHist([img2], channels = [0], mask = mask, histSize = [256], ranges = [0,256])
plt.figure()
plt.plot(masked_img_hist)
#channel değerlerini değiştirerek renklerin dağılımını görebiliriz.


#son olarak histogram eşitleme
#karşıtlık arttırma
img3 = cv2.imread("hist_equ.jpg",0)
plt.figure()
plt.imshow(img3, cmap = "gray")

#devam edelim histogram uygulayalım

img3_hist = cv2.calcHist([img3], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure()
plt.plot(img3_hist)

#eşitleme işlemi gerçekleştirelim
eq_hist = cv2.equalizeHist(img3)
plt.figure()
plt.imshow(eq_hist, cmap = "gray")

#koyu renklileleri 0'a çektik, açık renklileri 255'e çektik


eq_img3_hist = cv2.calcHist([eq_hist], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure()
plt.plot(eq_img3_hist)
#hist ile dar bölgeyi 0-255 arası genişlettik
#böylece renkler arasındaki karşıtlığı kullanarak resmimizin daha iyi anlaşılmasını sağlamış olduk








