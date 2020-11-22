# Enes Karacabay

import cv2

img = cv2.imread("foto.jpeg")#fotoyu okudum
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#griye dönüştürdüm
img_gray_blur = cv2.GaussianBlur(img_gray,(5,5),cv2.BORDER_DEFAULT)#blurladım(köşeler belli olsun diye)
_, thresh = cv2.threshold(img_gray_blur,150,230,cv2.THRESH_BINARY)##THRESH BINARY ya beyaz ya da siyah yapıyo
contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # Köşeleri alıyorsun

for cnt in contours: # tespit edilen köşeleri geziyoruz
    area = cv2.contourArea(cnt) ## köşeler arası uzaklık olabilir
    epsilon = 0.06 * cv2.arcLength(cnt, True) ##bununla sakın oynama yoksa bozuluyo
    approx = cv2.approxPolyDP(cnt,epsilon, True) ## Her şeklin köşe adresleri

    if area >400 : #
        cv2.drawContours(img,[approx],0,(0,0,255),2) ## tüm bulunan şekiller 2 kalınlıkta kırmızıya boyanır

        if len(approx)==4: ## 4 köşegeni olanlar burda ayrılıyor
            cv2.drawContours(img, [approx], 0, (0, 255, 255), 3)#Dörtgen olanlar Vurgulanıyor
            rect = img[approx[0][0][1]:approx[2][0][1],
                   approx[0][0][0]:approx[2][0][0]]###x1y1 x2y2 adresleri ile dörtgenleri kırpıyorum
            b = 0 # blue
            g = 0 # green
            r = 0


            for row in rect:
                for col in row:
                    b += col[0]
                    g += col[1]
                    r += col[2]
            o = rect.shape[0]*rect.shape[1]
            b = b//o
            g = g//o
            r = r//o
            ## bgr  ortalamalarını alıyorum

            if  10 < r < 40 and 100 < g < 130 and 130 < b < 200 :
                cv2.imwrite("pool.jpeg",rect)
                print("havuz fotoğrafı pool.jpeg adı ile kaydedildi ")
                ##istediğim ortalamada ise kaydediyorum

cv2.imwrite("image.jpeg", img) #Islem yapılmıs fotografi kaydediyorum 

