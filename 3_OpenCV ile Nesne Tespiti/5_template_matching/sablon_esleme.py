"""
Şablon Eşleme:
    Şablon eşleme yöntemini kullanarak nesne tespitinin nasıl yapılacağını öğreneceğiz.
    Şablon eşleştirme, bir şablon görüntünün konumunu daha büyük bir görüntüde aramak ve bulmak için bir yöntemdir.
    Şablon görüntüsünü giriş görüntüsünün üzerine kaydırır ve şablon görüntüsünün altındaki giriş göntüsünün şablonu ve yamayı karşılaştırır.
    
"""
"""
1-Kaydırarak, şablonu bir seferde bir piksel hareket ettirmeyi kastediyoruz.
(soldan sağa, yukarıdan aşağıya)
2-Her konumda, o konumdaki eşleşmenin ne kadar "iyi" veya "kötü" olduğunu
(veya şablonun kaynak görüntünün o belili alana ne kadar benzer olduğunu) temsil edecek şekilde bir metrik hesaplanır.

"""
import cv2
import matplotlib.pyplot as plt

# template matching: şablon eşleme
#(küçük resime şablon, büyük resime ise aramayı yapacağımız ana resim)

img = cv2.imread("cat.jpg", 0)
print(img.shape)
template = cv2.imread("cat_face.jpg", 0)
print(template.shape)
h, w = template.shape

methods = ["cv2.TM_CCOEFF", "cv2.TM_CCOEFF_NORMED", "cv2.TM_CCORR",
           "cv2.TM_CCORR_NORMED","cv2.TM_SQDIFF","cv2.TM_SQDIFF_NORMED"]
for meth in methods:
    method = eval(meth) #normal fonk çeviriyor stringleri
    
    res = cv2.matchTemplate(img, template, method)
    print(res.shape)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    cv2.rectangle(img, top_left, bottom_right,255,2)
    
    plt.figure()
    plt.subplot(121)
    plt.imshow(res, cmap = "gray")
    plt.title("Eslesen Sonuc")
    plt.axis("off")
    plt.subplot(122)
    plt.imshow(img, cmap = "gray")
    plt.title("Tespit Edilen Sonuc")
    plt.axis("off")
    plt.suptitle(meth)
    
    plt.show()
# openCV nin sağlamış olduğu 6 method var. bunların ortak amacı korelasyona bakmak
# iki resim arasındaki korelasyonu çıkarıyor