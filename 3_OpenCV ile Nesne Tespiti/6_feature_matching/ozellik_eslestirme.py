"""
Özellik Eşleştirme:
    Görüntü işlemeden nokta özelliği eşleşmesi, karmaşık bir sahnede belirtilen bir hedefi tespit ermek için etkili bir yöntemdir.
    Bu yöntem, birden çok nesne yerine tek nesneleri algılar.
    Örneğin, bu yöntemi kullanarak, kişi dağınık bir görüntü üzerinde belirli bir kişiyi tanıyabilir, ancak başka herhangi bir kişiyi tanıyamaz.
    
Brute-Force eşleştiricisi, bu görüntüdeki bir özelliğin tanımlayıcısı başka bir görüntünün diğer tüüm özellikleriyle eşleştirir ve mesageye göre eşleştirmeyi döndürür.
Tüm özelliklerle eşleşmeyi kontrol ettiği için yavaştır.

Ölçek değişmez özellik dönüşümü,anahtar noktaları ilk olarak bir dizi referans görüntüden çıkarılır ve saklanır.

Yeni görüntüdeki her bir özelliği bu saklanan veri ile ayrı ayrı karşılaştırarak ve öznitelik vektörlerinin Öklid mesafesine sayalı olarak aday eşleştirme özelliklerini bularak yeni bir görüntüde bir nesne tanınır.

"""
import cv2
import matplotlib.pyplot as plt

# ana görüntüyü içe aktar
chos = cv2.imread("chocolates.jpg",0)
plt.figure()
plt.imshow(chos, cmap = "gray")
plt.axis("off")

# aranacak olan görüntü 
cho = cv2.imread("nestle.jpg", 0)
plt.figure()
plt.imshow(cho, cmap = "gray")
plt.axis("off")

# orb tanımlayıcısı
# köşe-kenar gibi nesneye ait özellikler

orb = cv2.ORB_create()

#anahtar nokta tespiti
kp1, des1 = orb.detectAndCompute(cho, None)
kp2, des2 = orb.detectAndCompute(chos, None)

#bf matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING)
#noktaları eşleştir
matches = bf.match(des1, des2)

#mesafeye göre sırala
matches = sorted(matches, key = lambda x: x.distance)

#eşleşen resimleri görselleştir
plt.figure()
img_match = cv2.drawMatches(cho, kp1, chos, kp2, matches[:20], None, flags = 2)
plt.imshow(img_match)
plt.axis("off")
plt.title("orb")

# sift
# sift orb'ye göre biraz daha iyi
# sift openCV de kullanılan bir kütüphane olmasına rağmen dışarıdan openCV ye entegre edilmiş bir kütüphanedir

sift = cv2.xfeatures2d.SIFT_create()

#bf
bf = cv2.BFMatcher()

#anahtar nokta tespiti sift ile
kp1, des1 = sift.detectAndCompute(cho, None)
kp2, des2 = sift.detectAndCompute(cho, None)

matches = bf.knnMatch(des1,des2, k=2)

guzel_eslesme = []
for match1, match2 in matches:
    if match1.distance < 0.75*match2.distance:
        guzel_eslesme.append([match1])
plt.figure()
sift_matches = cv2.drawMatchesKnn(cho, kp1, chos, kp2, guzel_eslesme, None, flags = 2)
plt.imshow(sift_matches)
plt.axis("off")
plt.title("sift")





























