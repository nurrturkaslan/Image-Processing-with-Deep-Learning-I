"""
Görüntülerin Birleştirilmesi
Birden fazla görüntünün birleştirilmesini öğreneceğiz

Bu birleştirme iki tipli olacak:
1. elimizdeki bir resmi yanyana birleştireceğiz.
2. bu seferse alt alta- üst üste birleştşreceğiz.
"""

import cv2
import numpy as np

#resmi içe aktar
img = cv2.imread("lenna.png")
cv2.imshow("Orijinal", img)

#yanyana (horizontal)
hor = np.hstack((img, img))
cv2.imshow("Horizontal", hor)

#dikey(vertical)
ver  = np.vstack((img,img))
cv2.imshow("Vertical", ver)