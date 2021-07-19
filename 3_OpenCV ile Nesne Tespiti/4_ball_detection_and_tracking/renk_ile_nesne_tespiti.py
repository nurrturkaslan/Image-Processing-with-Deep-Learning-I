"""
Renk İle Nesne Tespiti:
    Belirli renklerde bulunan nesnelerin tespitinin nasıl yapılacağını kontur bulma yöntemi ile öğreneceğiz.
    Konturlar basitçe, aynı renk ve yoğunluğa sahip tüm sürekli noktaları birleştiren bir eğri olarak açıklanabilir.
    Konturlar, şekil analizi ve nesne algılama ve tanıma için kullanışlı bir araçtır.

RGB vs HSV

H(Hue): renk özü, renkler mavi, kırmızı, sarı .. vs
S(Saturation): Doygunluk
V(Value): Parlaklık
"""

import cv2
import numpy as np
from collections import deque
# deque' i bizim tespit ettiğimiz objenin merkezini depolamak için deque kullanacağız

#·nesne merkezine depolayacak veri tipi
buffer_size = 16 #►deque boyutu 16
pts = deque(maxlen = buffer_size) #pointler

# mavi renk aralığı HSV
blueLower = (84,98, 0)
blueUpper = ( 179, 255, 255)

#capture
cap = cv2.VideoCapture(0)
cap.set(3,960)
cap.set(4,480)

while True:
    
    success, imgOriginal = cap.read()
    
    if success:
        
        #blur
        blurred =cv2.GaussianBlur(imgOriginal, (11,11), 0)
        
        #hsv
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        
        cv2.imshow("HSV Image", hsv)
        
        #mavi için maske olusturacağız
        mask = cv2.inRange(hsv, blueLower, blueUpper)
        cv2.imshow("mask Image", mask)
        
        #erozyon ve genişleme işlemini ard arda yaparsak gürültüden arınırız
        mask = cv2.erode(mask, None, iterations = 2)
        mask = cv2.dilate(mask, None, iterations = 2)
        cv2.imshow("mask + erozyon ve genişleme", hsv)
        
        #konturleri bulma
        (_, contours, _) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        center =  None
        
        if len(contours) > 0:
            # en büyük konturu al
            c= max(contours, key = cv2.contourArea)
            
            # dikdörtgene çevir
            rect = cv2.minAreaRect(c)
            
            ((x,y), (width, height), rotation) = rect
            
            s = "x: {}, y: {}, width: {}, height: {}, rotation: {}".format(np.round(x),np.round(y),np.round(width),np.round(height),np.round(rotation))
            print(s)
            
            box = cv2.boxPoints(rect)
            box = np.int64(box)
            
            # moment
            M = cv2.moments(c)
            center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))
            
            # konturu çizdirelim: sarı
            cv2.drawContours(imgOriginal, [box], 0, (0,255,255), 2)
            
            #merkeze bir tane nokta çizdirelim: pembe
            cv2.circle(imgOriginal, center, 5, (255,0,255),-1)
            
            #bilgileri ekrana yazdır
            cv2.putText(imgOriginal, s, (25,25), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 2)
            
            #deque
            pts.appendleft(center)
            
            for i in range(1, len(pts)):
                if pts[i-1] is None or pts[i] is None: continue
            
            cv2.line(imgOriginal, pts[i-1],pts[i], (0,255,0),3)
            
        cv2.imshow("Original Tespit", imgOriginal)
            
            
            
            
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break