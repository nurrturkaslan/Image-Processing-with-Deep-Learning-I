"""
Gradyanlar:
    Görüntü gradyanı, görüntüdeki yoğunluk veya renkteki yönlü bir değişikliktir.
    Kenar algılamada kullanılır.
"""
import cv2
import matplotlib.pyplot as plt

#resmi içe aktar
img = cv2.imread("sudoku.jpg", 0)
plt.figure()
plt.imshow(img, cmap = "gray")
plt.axis("off")
plt.title("Orijinal Img")

# x gradyan
sobelx = cv2.Sobel(img, ddepth = cv2.CV_16S, dx = 1, dy = 0, ksize = 5) 
#ddepth parametresi ouput un derinliğini gösteriyor
plt.figure()
plt.imshow(sobelx, cmap = "gray")
plt.axis("off")
plt.title("Sobel X")
# dik olan kenarlarımızı tespit etmiş olduk yukarıdaki kod parçacıklarında.


#şimdi ise y'sini yapalım yatay kenarlarımızı tespit edelim.
sobely = cv2.Sobel(img, ddepth = cv2.CV_16S, dx = 0, dy = 1, ksize = 5) 
#ddepth parametresi ouput un derinliğini gösteriyor
plt.figure()
plt.imshow(sobely, cmap = "gray")
plt.axis("off")
plt.title("Sobel Y")


#şimdi ise her ikisinide tespit etmeye çalışalım.
#laplacian gradyan kullanacağız.

laplacian = cv2.Laplacian(img, ddepth = cv2.CV_16S)
plt.figure()
plt.imshow(laplacian, cmap = "gray")
plt.axis("off")
plt.title("Laplacian")