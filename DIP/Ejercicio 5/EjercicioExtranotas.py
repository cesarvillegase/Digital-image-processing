# Manipulación de imágenes e información
#Elaborado por César Alejandro Villegas Espíndola

#Se importan las librerias
import cv2 #Se importa cv2 para cargar la imagen
from matplotlib import pyplot #Para poder hacer gráficos
import numpy as np #Para encargarnos de las matrices

#Para ver el arreglo de intensidad del RGB por cada pixel de la imagen 
print(cv2.imread('/Users/cvillegas/workspace/Py/DIP/Ejercicio 5/car.jpeg'))

#Se define la función de rotación de matriz, lo cual toma cierta cantidad de grados
def rot_mat(deg):
    theta=deg/180*np.pi #Numpy no toma grados por lo que debemos de convertir los grados a radianes
    c,s=np.cos(theta),np.sin(theta) #Se precalculan los valores de seno y coseno
    return np.array([[c,-s],[s,c]]) #Se regresa la matriz de rotación que sera un arreglo

#Para leer la imagen con opencv
im = cv2.imread('/Users/cvillegas/workspace/Py/DIP/Ejercicio 5/car.jpeg')
#Se convierte la imagen de BGR a RGB porque por defecto cv2 espera la imagen como BGR
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)

#Graficación de la imagen sin modificar
pyplot.plot(111)
pyplot.imshow(im)
pyplot.show()

#Cantidad de grados de la rotación de matriz, en este caso se indica que se rotara 180 grados.
deg=180 
h,w,c = im.shape #Heigth, width y chanels
h2,w2=h//2,w//2 #H2 es la mitad de la altura y w2 es la mitad del ancho, es el porque da igual a h entre 2 y w entre 2.

#Mitad del Ancho rotado y mitad del largo rotado igual al valor máximo, Se busca que sea un valor abs
#rot_mat que esta toma ña cant. de grados y la matriz multiplica. Lo que se busca es el valor maximo de
#las coordenadas x y y de los puntos los cuales son superior izquierdo, superior derecho y inferior derecho.
wr2,hr2=(np.max(np.abs(rot_mat(deg) @ np.array([[-w2,w2,w2],[h2,h2,-h2]])),axis=1)).astype(np.int32)
wr,hr=wr2*2,hr2*2 #

#Esto se hace para obtener la img rotada
imr=np.zeros((hr,wr,3)).astype(np.int32) #Se tuvo que hacer entero porque no reconocia el valor flotante

yr,xr=np.indices((hr,wr))
yr,xr=yr.flatten(),xr.flatten()
yrc,xrc=yr-hr2,xr-wr2
xc,yc=(rot_mat(-deg) @ np.row_stack((xrc,yrc))).astype(np.int32)
x,y=xc+w2,yc+h2
include=np.logical_and(np.abs(xc)<w2,np.abs(yc)<h2)

include.mean()

imr[yr[include],xr[include]]=im[y[include],x[include]]

#Fig2 es para presentar la imagen sin rotar y la imagen rotada
fig2=pyplot.subplot(311)
fig2=pyplot.imshow(im)

fig2=pyplot.subplot(312)
fig2=pyplot.imshow(imr)

fig2=pyplot.show()

#Elaborado con la ayuda de: https://www.youtube.com/watch?v=hU_2pZxmQVU&ab_channel=Charlie
#Se arreglo el problema de un float en la linea 27 con: https://stackoverflow.com/questions/49643907/clipping-input-data-to-the-valid-range-for-imshow-with-rgb-data-0-1-for-floa