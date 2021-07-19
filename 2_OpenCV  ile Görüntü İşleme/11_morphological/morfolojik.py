
"""
Morfolojik Operasyonlar

Erozyon, genişleme, açma, kapatma ve morfolojik gradyan gibi morfolojik operasyonların ne olduklarını öğreneceğiz.
"""

"""
Erozyon:
    Erozyonun temel fikri sadece toprak erozyonu gibidir, ön plandaki nesnenin sınırlarını aşındırır.

Genişleme:
    Erozyonun tam tersidir.
    Görüntüdeki beyaz bölgeyi arttırır.
    
Açma:
    Açılma, erozyonun + genişlemedir.
    Gürültünün giderilmesinde faydalıdır.
    Ön plandaki nesnelerin içindeki küçük delikleri veya nesne üzerindeki küçük siyah noktaları kapatmak için kullanışlıdır.

Morfolojik Gradyan:
    Bir görüntünün genişlemesi ve erozyonu arasındaki farktır.
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

#resmi içe aktar
img = cv2.imread("datai_team.jpg", 0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("Orijinal Image")

#erozyon
#sınırlarımızı küçültüyoruz

kernel = np.ones((5,5), dtype = np.uint8)
result = cv2.erode(img, kernel, iterations = 1)
#iterations =1 1 kere erozyon yap, 2 yaparsak biraz daha küçülecek, 5 yaparsak tamamen erozyona uğrayacak
plt.figure(), plt.imshow(result, cmap = "gray"), plt.axis("off"), plt.title("Erozyon Image")



#şimdi ise erozyonun tersi ile devam ediyoruz:
    #erozyonun tersi genişleme(dilation)
result2 = cv2.dilate(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result2, cmap = "gray"), plt.axis("off"), plt.title("Genisleme Image")

#Açılma: 
#Gürültüyü azaltmak için beyaz gürültüyü azaltmak için uyguluyoruz.
#Bunun için bir beyaz gürültü oluşturalım ki resmimize beyaz gürültü ekleyelim.

#white noise

whiteNoise = np.random.randint(0,2, size = img.shape[:2])
whiteNoise = whiteNoise*255 #istediğimiz sıkalaya çıkaramak için *255
plt.figure(), plt.imshow(whiteNoise, cmap = "gray"), plt.axis("off"), plt.title("WhiteNoise Image")

#şimdi ne yapacağız bu gürültüyü orijinal resmimin üzerine ekleyeceğiz.
noise_img = whiteNoise + img
plt.figure(), plt.imshow(noise_img, cmap = "gray"), plt.axis("off"), plt.title("WhiteNoise Image with whiteNoise") 

#şimdi bu noise'u açılma yöntemi ile ortadan kaldıracağız
# Açılma:
    
openning = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)   
plt.figure(), plt.imshow(openning, cmap = "gray"), plt.axis("off"), plt.title("Acilma")  


#şimdi ise açılmanın tersi ile devam edelim
#Kapatma:
#Ama kapatmayı yapabilmek için bizim bir noise'a ihtiyacımız var
#Bu seferde

#blackNOise elde edeceğiz
blackNoise = np.random.randint(0,2, size = img.shape[:2])
blackNoise = blackNoise*-255 #siyah noise * -255
plt.figure(), plt.imshow(blackNoise, cmap = "gray"), plt.axis("off"), plt.title("BlackNoise Image")

black_noise_img = blackNoise + img
black_noise_img[black_noise_img <= -245] = 0
plt.figure(), plt.imshow(black_noise_img, cmap = "gray"), plt.axis("off"), plt.title("Black Noise Image")

#kapatma yöntemini kullanarak şimdi black noise'dan kurtulabiliriz.
closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)   
plt.figure(), plt.imshow(openning, cmap = "gray"), plt.axis("off"), plt.title("Kapatma")  

#morfolojik gradyan operasyonu
#genişleme ile erozyon arasındaki farkı alıyoruz.
gradient = cv2.morphologyEx(img.astype(np.float32), cv2.MORPH_GRADIENT, kernel)   
plt.figure(), plt.imshow(gradient, cmap = "gray"), plt.axis("off"), plt.title("Gradyan")  

















