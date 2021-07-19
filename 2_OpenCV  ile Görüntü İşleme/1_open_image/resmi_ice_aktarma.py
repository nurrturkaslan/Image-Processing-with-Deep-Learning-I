"""
OpenCV ile Görüntü İşlemeye Giriş
OpenCV python dilinde hatta diğer dillerde de görüntü işleme alanında kullanılan önemli kütüphanelerden bir tanesidir.

Bizde OpenCV kütüphanesini kullanarak görüntü işleme temellerini ele alacağız.

Resmi içe aktarma,
Video içe aktarma,
Kamera açma ve Video Kaydı,
Yeniden boyutlandır kırp,
Şekiller ve metin,
Görüntülerin Birleştirilmesi,
Perspektif Çarpıtma,
Görüntüleri karıştırmak,
Görüntü Eşikleme,
Bulanıklaştırma,
Morfolojik Operasyonlar,
Grandyanlar,
Histogram
"""


"""
Resmi İçe Aktarma
Görselin nasıl okunacağını, nasıl görüntüleneceğini ve nasıl kaydedileceğini öğreneceğiz.
"""

import cv2 #buradaki cv computer vision'dan gelmektedir.

#içe aktarma
img = cv2.imread("messi5.jpg", 0) # 0 ise "gray scale" olarak resmi import etmemi, içe aktarmamı sağlıyor. Yani siyah ve beyazlardan oluşan resim anlamına gelir.
img

#görselleştir
cv2.imshow("ilk resim", img)

"""
Bu resimdeki sayılar her bir pikselin sahip olduğu genlik.
yani piksel değeridir.
Buradaki sayılar 0 ile 255 arasında değişen sayılardır.
280'e 450 boyutunda bir arraydir. Size kısmında yer alan (280,450)
Her bir array'in elemanı piksel anlamına geliyor.
Burada eğer console kısmında 250*450 yaparsak 126000 tane piksel var.
Bu piksellerin içerisinde bulunan değerlerde bu piksellerin;
genlipi anlamına geliyor. Biz resimleri bu şekilde ifade ediyoruz.
Aslında resim dediğimiz şey tamamen iki boyuttan oluşan matrislerdir.
"""
k = cv2.waitKey(0)&0xFF

if k == 27: # bu ise klavyedeki esc tuşunun değeri kodu çalıştırdıktan sonra resmi kapatmamıza yarıyor.
    cv2.destroyAllWindows()
elif k == ord("s"): #klavyedeki "s" kodu çalıştırınca s'ye bastığımızda siyah-beyaz resim oluşturacaktır.
    cv2.imwrite("messi_gray.png", img)
    cv2.destroyAllWindows()