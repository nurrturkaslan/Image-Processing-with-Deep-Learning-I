"""
Yüz Tanıma Projesi:
    Yüz algılama, dijital görüntüdeki insan yüzlerini tanımlayan,
    çeşitli uygulamalarda kullanılan yöntemdir.
    
1-Haar özelliği tabanlı kademeli sınıflandırıcıları kullanan Nesne Algılama,
Paul Viola ve Michael Jones tarafından 2001 yılında "Yükseltilmiş Basit Özellikler Basamaklı Kullanılarak Hızlı Nesne Algılama"
başlıklı makalesinde önerilen etkili bir nesne algılama yöntemidir.

2-Benzer özellikler işlevi, birçok pozitif ve nagatif görüntüden eğitilir.
yüz içeren (pozitif görüntü), içermeyen (negatif görüntü)

3-Daha sonra diğer görüntülerdeki nesneleri tespit etmek için kullanılır.
(a) Edge Features(Kenar)
(b) Line F.(Çizgi)
(c) Four-rectange F.(Dört tane rectangle dan oluşan features)

4-Bunun için aşağıdaki görselde gösterilen Haar özellikleri kullanılmaktadır.

5-Tıpkı evrişimli çekirdeğimiz gibiler. Her özellik,
siyah dikdörtgenin altındaki piksellerin toplamından beyaz dikdörtgenin
altındaki piksellerin toplamlarının çıkarılmasıyla elde edilen tek bir değerdir.

"""

import cv2
import matplotlib.pyplot as plt

# içe aktar
einstein = cv2.imread("einstein.jpg", 0)
plt.figure()
plt.imshow(einstein, cmap = "gray")
plt.axis("off")

# sınıflandırcı: yüz olup olmamasını sınıflandırıyor
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face_rect = face_cascade.detectMultiScale(einstein)

for (x, y, w, h) in face_rect:
    cv2.rectangle(einstein, (x,y), (x+w, y+h),(2555,255,255),10)
plt.figure()
plt.imshow(einstein, cmap = "gray")
plt.axis("off")

# barcelona
# içe aktar
barce = cv2.imread("barcelona.jpg", 0)
plt.figure()
plt.imshow(barce, cmap = "gray")
plt.axis("off")

face_rect = face_cascade.detectMultiScale(barce, minNeighbors = 7)

for (x, y, w, h) in face_rect:
    cv2.rectangle(barce, (x,y), (x+w, y+h),(2555,255,255),10)
plt.figure()
plt.imshow(barce, cmap = "gray")
plt.axis("off")
#minNeigbors değerini arttırarak daha doğru bir yüz tespiti yapmıs oluruz.

#video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if ret:
        face_rect = face_cascade.detectMultiScale(barce, minNeighbors = 7)
        
        for (x, y, w, h) in face_rect:
            cv2.rectangle(barce, (x,y), (x+w, y+h),(2555,255,255),10)
        cv2.imshow("face detect", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()



















