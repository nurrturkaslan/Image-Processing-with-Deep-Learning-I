"""
Yeniden Boyutlandırma ve Kırpma
"""
import cv2

# içe aktarma

#boyutlandıma
img = cv2.imread("lenna.png") # 0 siyah-beyaz
print("Resim Boyutu: ", img.shape)
cv2.imshow("Orijinal", img)

imgResized  = cv2.resize(img, (800,800))
print("Resized Img Shape: ", imgResized.shape)
cv2.imshow("Img Resized", imgResized)

#kırpma
imgCropped = img[:200,:300] #width height -> height width
cv2.imshow("Kirpik Resim", imgCropped)