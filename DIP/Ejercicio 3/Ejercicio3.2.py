#Operaciones en imágenes
#Elaborado por César Alejandro Villegas Espíndola

#Se importaron las siguientes librerias
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#Se cargo la imagen a trabajar
img = mpimg.imread('/Users/cvillegas/workspace/Py/DIP/Ejercicio 3/Cat3.jpg')

#===============================RGB===============================
img2 = np.zeros((1200,1600,3), dtype=np.uint8)
img3 = np.zeros((1200,1600,3), dtype=np.uint8)
img4 = np.zeros((1200,1600,3), dtype=np.uint8)

#Separar los canales RGB
#Rojo canal 0 es el R, Canal 1 es el G, y el canal 2 el B

#Rojo
red = img[:,:,0]
green = img[:,:,1]
blue = img[:,:,2]

green =0*green
blue =blue*0

img2[:,:,0]=red
img2[:,:,1]=green
img2[:,:,2]=blue

#Verde
red = 0*img[:,:,0]
green = img[:,:,1]
blue = 0*img[:,:,2]

img3[:,:,0]=red
img3[:,:,1]=green
img3[:,:,2]=blue

#Azul
red = 0*img[:,:,0]
green = 0*img[:,:,1]
blue = img[:,:,2]

img4[:,:,0]=red
img4[:,:,1]=green
img4[:,:,2]=blue

#Generación de subplots
f, axes = plt.subplots(2,2, constrained_layout = True)
axes[0, 0].title.set_text('Normal')
axes[0, 0].imshow(img)
axes[0, 1].title.set_text('Red')
axes[0, 1].imshow(img2)
axes[1, 0].title.set_text('Green')
axes[1, 0].imshow(img3)
axes[1, 1].title.set_text('Blue')
axes[1, 1].imshow(img4)
plt.show()

#CMY
img5 = np.zeros((1200,1600,3), dtype=np.uint8) #Imagen completa en negativo
img6 = np.zeros((1200,1600,3), dtype=np.uint8)
img7 = np.zeros((1200,1600,3), dtype=np.uint8)
img8 = np.zeros((1200,1600,3), dtype=np.uint8)

#Conversion a espacio CMY

img5[:,:,0]=255-img[:,:,0]
img5[:,:,1]=255-img[:,:,1]
img5[:,:,2]=255-img[:,:,2]

#Cyan
red = 255-img[:,:,0]
green = 255
blue = 255

img6[:,:,0]=red
img6[:,:,1]=green
img6[:,:,2]=blue

#Magenta
red = 255
green = 255-img[:,:,1]
blue = 255

img7[:,:,0]=red
img7[:,:,1]=green
img7[:,:,2]=blue

#Yellow
red = 255
green = 255
blue = 255-img[:,:,2]

img8[:,:,0]=red
img8[:,:,1]=green
img8[:,:,2]=blue

f, axes = plt.subplots(2,2, constrained_layout = True)
axes[0, 0].title.set_text('Normal')
axes[0, 0].imshow(img5)
axes[0, 1].title.set_text('Cyan')
axes[0, 1].imshow(img6)
axes[1, 0].title.set_text('Magenta')
axes[1, 0].imshow(img7)
axes[1, 1].title.set_text('Yellow')
axes[1, 1].imshow(img8)
plt.show()