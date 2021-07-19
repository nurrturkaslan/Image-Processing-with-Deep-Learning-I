"""
Kontur Algılama:
    Kontur tespiti, atnı renk veya yoğunluğa sahip tüm kesintisiz
    noktaları (sınırla birlikte) birleştirmeyi amaçlayan yöntemdir.
    
    Konturlar şekil analizi ve nesne algılama ve tanıma için kullanılır.
    
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

#resmi içe aktar
img = cv2.imread("contour.jpg", 0)
plt.figure()
plt.imshow(img, cmap = "gray")
plt.axis("off")

#kontur tespiti
image, contours, hierarch = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

external_contour = np.zeros(img.shape)
imternal_contour = np.zeros(img.shape)                        

for i in range(len(contours)):
    
    #external
    if hierarch[0][i][3] == -1:
        cv2.drawContours(external_contour, contours, i, 255, -1)# 255 renk, -1 kalınlık
    else: #internal
        cv2.drawContours(internal_contour, contours, i, 255, -1)
plt.figure()
plt.imshow(external_contour, cmap = "gray")
plt.axis("off")

plt.figure()
plt.imshow(internal_contour, cmap = "gray")
plt.axis("off") 