"""
Köşe Algılama:
    Özellik Nedir?
    Bigisayarlarla görmede, genellikle bir resmin/videonun farklı çerçeveleri arasında
    eşleşen noktalar bulmanız gerekir. Çünkü, iki görüntünün birbiriyle nasıl ilişkili olduğunu bilirsek,
    her iki görüntüyüde bilgi almak için kullanabiliriz.,
    
    Eşleştirme noktaları dediğimizde genel anlamda sahnedeki kolayca tanıyabileceğimiz özelliklere atıfta bulunuyoruz.
    Bu özelliklere özellikler diyoruz.
    
    Bu özellikler benzersiz bir şekilde tanılabilir olmalıdır.
    
    Temel Özellikler Nelerdir?
    Kenarlar
    Köşeler
    
    Köşe Algılama,
    köşeler iki kenarın kesişimi olduğu için bu iki kenarın yönlerinin değiştiği noktayı temsil eder.
    
    Köşeler, resimdeki renk geçişindeki bir varyasyonu temsil ettiğinden, bu "varyasyonu" arayacağız.
    Görüntü yoğunluğundaki varyasyonu arayacağız
    
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

#resmi içe aktar
img = cv2.imread("sudoku.jpg", 0)
img = np.float32(img)
print(img.shape)
plt.figure()
plt.imshow(img, cmap = "gray")
plt.axis("off")

#harris corner detection
dst = cv2.cornerHarris(img, blockSize = 2, ksize = 3, k = 0.04)
#buradaki blockSize: komşuluk boyutu
#ksize: şimdiye kadar kullandığımız kutucuğun boyutu
plt.figure()
plt.imshow(dst, cmap = "gray")
plt.axis("off")

dst = cv2.dilate(dst, None)
img[dst>0.2*dst.max()] = 1
plt.figure()
plt.imshow(dst, cmap = "gray")
plt.axis("off")

# ☺şimdi farklı bir kenar algılama yöntemi ile devam edelim

#shi tomasi detection
img = cv2.imread("sudoku.jpg", 0)
img = np.float32(img)
corners = cv2.goodFeaturesToTrack(img, 120, 0.01,10)
corners = np.int64(corners)
# buradaki 100: kaç tane köşe istediğimiz(yani 100 köşe tespit edeceğiz)
# 0.01: ise quality level
#10: iki köşe arası minimum distıns

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,(125,125,125),cv2.FILLED)
    
plt.imshow(img)
plt.axis("off")   



















