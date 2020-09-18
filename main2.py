import cv2
import string
import numpy as np


print ("Pruebas con Open Cv")
print ("-------------------------------")
print ("-------------------------------")
print ("---Opciones disponibles--------")
print("a = Deteccion facial  || b = Deteccion de bordes con Sobel")
print("La opcion a guarda una imagen en escala de grises del rostro capturado")
resp = input("Elije que funcionalidad deseas probar: ")

if resp == "a":
    cap = cv2.VideoCapture(0)

    faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_gray = gray[y: y + h, x: x + w] #region of interest
            roi_color = frame[y: y + h, x: x + w]
            img_item = "my-image.png"
            cv2.imwrite(img_item, roi_gray)

        cv2.imshow('frame', frame)
        cv2.imshow('video gray', grayFrame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
else:
    video = cv2.VideoCapture(0)
    while   True:
        ret, frame1 = video.read()
        frame = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
        frame_float = frame.astype(float)
        #KERNEL DE SOBEL
        Hsx = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
        Hsy = np.transpose(Hsx)
        #BORDES  EN  LAS  DIRECCIONES  HORIZONTALES  Y  VERTICALES
        bordex = cv2.filter2D(frame_float, -1, Hsx)
        bordey = cv2.filter2D(frame_float, -1, Hsy)
        #CALCULO DE LA MAGNITUD DEL GRADIENTE
        Mxy = bordex**2 + bordey**2 #OPERACION PIXEL POR PIXEL
        Mxy = np.sqrt(Mxy)
        #NORMALIZACION
        Mxy = Mxy/np.max(Mxy)
        #SEGMENTACION
        mask = np.where(Mxy>0.1, 255, 0)
        mask = np.uint8(mask)
        cv2.imshow('BORDES', mask)
        k = cv2.waitKey(1)&0xFF
        if(k == ord('q')):
            print('ACABO EL PROGRAMA')
            break
    video.release()
    cv2.destroyAllWindows()
