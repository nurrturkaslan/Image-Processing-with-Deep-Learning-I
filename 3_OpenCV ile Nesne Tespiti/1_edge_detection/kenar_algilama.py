"""
Kenar Algılama:
    Görüntü parlaklığının keskin bir şekilde değiştiği,
    noktaları tanımlamayı amaçlayan yöntemdir.
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

#resmi içe aktar

img= cv2.imread("london.jpg", 0)
plt.figure()
plt.imshow(img, cmap = "gray")
plt.axis("off")

#şimdi herhangi bir eşik değer belirlemeden kenarları tespit etmeye başlayalım

edges = cv2.Canny(image = img, threshold1 = 0, threshold2 = 255)
plt.figure()
plt.imshow(edges, cmap = "gray")
plt.axis("off")
#aslında bir threshold belirlemedim zaten benim resmim 0 ile 255 arasında
#herhangi bir threshold kullanmadığımız için neredeyse tüm kenarları ortaya çıktı.

med_val = np.median(img)
print(med_val)

low = int(max(0, (1 - 0.33)*med_val))
high = int(min(255, (1 + 0.33)* med_val))

print(low)
print(high)

edges = cv2.Canny(image = img, threshold1 = low, threshold2 = high)
plt.figure()
plt.imshow(edges, cmap = "gray")
plt.axis("off")

#blur
blurred_img = cv2.blur(img, ksize = (3,3))
plt.figure()
plt.imshow(blurred_img, cmap = "gray")
plt.axis("off")

edges = cv2.Canny(image = blurred_img, threshold1 = low, threshold2 = high)
plt.figure()
plt.imshow(edges, cmap = "gray")
plt.axis("off")
