"""
Bulanıklaştırma

Görüntü bulanıklığı, görüntünün düşük geçişli bir filtre uygulanmasıyla elde edilir.
Gürültüyü gidermek için kullanışlıdır. 
Aslında görüntüden yüksek frekanslı içeriği(örneğin: parazit, kenarlar) kaldırır.
OpenCV, üç ana tür bulanıklaştırma tekniği sağlar.
Ortalama Bulanıklaştırma
Gauss Bulanıklaştırma
Medyan Bulanıklaştırma
"""

"""
Ortalama Bulanıklaştırma:
Bir görüntünün normalleştirilmiş bir kutu filtresiyle sarılmasıyla yapılır.
Çekirdek alanı altındaki tüm piksellerin ortalamasını alır ve bu ortalamayı merkezi öğe ile yer değiştirir.

Gauss Bulanıklaştırma:
Bu yöntemde kutu filtresi yerine Gauss çekirdeği kullanılır.
Pozitif ve tek olması gereken çekirdeğin genişliği ve yükseliği belirtilir.
SigmaX ve sigmaY , X ve Y yönlerindeki standart sapmayı belirtmeliyiz.

Medyan Bulanıklaştırma:
Çekirdek alanı altındaki tüm piksellerin medyanını alır ve merkezi öğe bu medyan değerle değiştirilir.
Tuz ve biber gürültüsüne karşı oldukça etkilidir.
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")

# blurring(detayı azaltır, gürültüyü engeller)
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img), plt.axis("off"), plt.title("orijinal"), plt.show()

"""
Ortalama Bulanıklaştırma Yöntemi
"""
dst2 = cv2.blur(img, ksize = (3,3))
plt.figure()
plt.imshow(dst2) #opencv de çıktılar dst girdiler img kısmı source yani src olarak adlandırılıyor.
plt.axis("off")
plt.title("ortalama blur")

"""
Gauss Bulanıklaştırma Yöntemi
"""
gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title("gauss blur")

"""
Medyan Bulanıklaştırma Yöntemi
"""
mb = cv2.medianBlur(img, ksize = 3)
plt.figure()
plt.imshow(mb)
plt.axis("off")
plt.title("median blur")


def gaussianNoise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    
    return noisy

# ice aktar ve normalize et
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
plt.figure()
plt.imshow(img), plt.axis("off"), plt.title("orijinal"), plt.show()

gaussianNoisyImage = gaussianNoise(img)
plt.figure()
plt.imshow(gaussianNoisyImage)
plt.axis("off")
plt.title("Gaussian Noisy")
plt.show()

# gauss blur
gb2 = cv2.GaussianBlur(gaussianNoisyImage, ksize = (3,3), sigmaX = 7)
plt.figure()
plt.imshow(gb2)
plt.axis("off")
plt.title(" with gauss blur") #noisy azaltma, detay azaltma



# Medyan Bulur
def saltPepperNoise(image):
    
    row, col, ch = image.shape
    s_vs_p = 0.5

    amount = 0.004
    
    noisy = np.copy(image)
    
    #salt beyaz noktacıklar eklenecek
    num_salt = np.ceil(amount * image.size*s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))for i in image.shape]
    noisy[coords] = 1 #beyaz 1 siyah 0
    
    #pepper siyah
    num_pepper = np.ceil(amount * image.size* (1 - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))for i in image.shape]
    noisy[coords] = 0 #beyaz 1 siyah 0
    
    return noisy
    
spImage = saltPepperNoise(img)
plt.figure()
plt.imshow(spImage)
plt.axis("off")
plt.title("sp Image")

mb2 = cv2.medianBlur(spImage.astype(np.float32), ksize = 3)
plt.figure()
plt.imshow(mb2)
plt.axis("off")
plt.title("spImage median blur") #noisy yok oldu



