import cv2

imagen = cv2.imread('yeah.jpg')

grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
bordes = cv2.Canny(grises, 100, 200)

cv2.imshow('Bordes', bordes)
cv2.imshow('Imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("Holi")
