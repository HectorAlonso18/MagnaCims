import cv2
import numpy as np

#Abrir cámara
cap = cv2.VideoCapture(1)

#Tomar foto
ret, foto = cap.read()

#Mostrar foto
cv2.imshow('Imagen capturada', foto)

output = foto.copy()
img = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.3, 100)
pix=0.10185731

#Encontrar circulos
if circles is not None:
    #Obtener (x, y, d) como enteros
    circles = np.round(circles[0, :]).astype("int")
    print(circles)
    #Crear lista de radios encontrados
    rad = []

    for (x, y, d) in circles:
        # Append the radius value to the rad list
        rad.append(float(d))
        cv2.circle(output, (x, y), d, (0, 255, 0), 2)

    rad = np.array(rad)
    listarad = rad * pix
    listarad = np.round(listarad,4)
    print("Los diámetros de sus círculos son: ")
    
    for elemento in listarad:
        print(elemento)
   
else:
   print("No se han encontrado círculos")

if elemento >=12 and elemento <=14 and elemento >=5 and elemento <=6:
    print("correcto")

else:
    print("incorrecto")
   
#Mostrar imagen capturada con círculos
cv2.imshow("circle",output)
cv2.waitKey(0)
cv2.destroyAllWindows()