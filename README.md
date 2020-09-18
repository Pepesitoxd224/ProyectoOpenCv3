# ProyectoOpenCv3

## Descripción
Nuestro proyecto consiste en tres fases: la primera, utilizando la cámara del dispositivo abre dos ventanas, en las que se observa la cámara frontal tanto en escala de grises como a color. Posteriormente, añadimos un algoritmo para el reconocimiento facial que se basa en la misma cámara, para que así detecte la cara de las personas que aparezcan en pantalla, o bien, los rostros de las personas en una imagen. A esto le agregamos una función para que al salir del programa, se guarden dos imágenes nuevas en la carpeta, siendo estas la parte de interés de la cámara, es decir, la cara de las personas, que nuevamente se guarda tanto a color como en escala de grises. Por último, en la tercera fase implementamos un algoritmo para la detección de bordes con base en el modelo de Sobel, que funciona tanto para la cámara en "vivo" o para el procesamiento de cualquier imagen elegida. 

## Capturas de pantalla.

Captura del menu en la consola al ejecutar el programa.
![imagen del menu](https://raw.githubusercontent.com/Pepesitoxd224/ProyectoOpenCv3/master/capturas/ssmenu.PNG)

En caso de presionar "b", despliega lo siguiente.
![imagen opcion b](https://raw.githubusercontent.com/Pepesitoxd224/ProyectoOpenCv3/master/capturas/ssSobelOpb.PNG)

En caso de presionar "a", despliega lo siguiente.
![imagen opcion a](https://raw.githubusercontent.com/Pepesitoxd224/ProyectoOpenCv3/master/capturas/ssOpA.PNG)

Cuando se presiona la opcion "a", se guardan dos imagenes del rostro detectado, una a color y otra en escala de grises.
![imagen resultados opcion a](https://raw.githubusercontent.com/Pepesitoxd224/ProyectoOpenCv3/master/capturas/my-image_gray.png)
![imagen resultados opcion a](https://raw.githubusercontent.com/Pepesitoxd224/ProyectoOpenCv3/master/capturas/my-image_Color.png)

## Repos utilizados:
- Open CV para el xml (https://github.com/opencv/opencv)
- Digital image processing (https://github.com/jorgepdsML/DIGITAL-IMAGE-PROCESSING-PYTHON)
- Conerting webcam video to grayscale (https://techtutorialsx.com/2019/04/13/python-opencv-converting-webcam-video-to-gray-scale/)

La versión del programa que utilizamos fue Python 3.8.5.


