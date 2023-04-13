import numpy as np
import cv2
 
# Cargamos la imagen
original = cv2.imread("C:/Users/mmhur/Pictures/barrenos.jpeg")
cv2.imshow("original", original)

# Convertimos a escala de grises
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
 
# Aplicar suavizado Gaussiano
gauss = cv2.GaussianBlur(gris, (5,5), 0)
 
cv2.imshow("suavizado", gauss)

# Detectamos los bordes con Canny
canny = cv2.Canny(gauss, 50, 150)
 
cv2.imshow("canny", canny)

# Buscamos los contornos
(contornos, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filtramos los contornos para quedarnos solo con los circulares
circulares = []
for c in contornos:
    perimetro = cv2.arcLength(c, True)
    aprox = cv2.approxPolyDP(c, 0.03*perimetro, True)
    if len(aprox) > 8:
        circulares.append(c)

# Mostramos el número de círculos por consola
print("He encontrado {} circulos".format(len(circulares)))

cv2.drawContours(original, circulares, -1, (0, 0, 255), 2)
cv2.imshow("contornos circulares", original)

cv2.waitKey(0)
cv2.destroyAllWindows()
