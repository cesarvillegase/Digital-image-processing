#Examen 
#Elaborado por César Alejandro Villegas Espíndola
#Fecha: Jueves 10 de noviembre del 2022

#Importación de librerias 
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

#Se carga la imagen 
img = mpimg.imread('/Users/cvillegas/workspace/Py/DIP/Examen /imagenog1.jpg')
img2 = mpimg.imread('/Users/cvillegas/workspace/Py/DIP/Examen /imagenog2.jpg')

# A) Mostrar una sola imagen cuyo los dos primeros canales 
# Sean de rg y de la segunda imagen seria el tercer canal b

img1_2 = np.zeros((1080,1920,3), dtype=np.uint8)
img1_3 = np.zeros((1080,1920,3), dtype=np.uint8)
img1_4 = np.zeros((1080,1920,3), dtype=np.uint8)

#Rojo
red = img[:,:,0]
green = img[:,:,1]
blue = img[:,:,2]

green =0*green
blue =blue*0

img1_2[:,:,0]=red
img1_2[:,:,1]=green
img1_2[:,:,2]=blue

#Verde
red = 0*img[:,:,0]
green = img[:,:,1]
blue = 0*img[:,:,2]

img1_3[:,:,0]=red
img1_3[:,:,1]=green
img1_3[:,:,2]=blue

#Azul
red = 0*img2[:,:,0]
green = 0*img2[:,:,1]
blue = img2[:,:,2]

img1_4[:,:,0]=red
img1_4[:,:,1]=green
img1_4[:,:,2]=blue

img_md1 = img1_2 + img1_3 + img1_4

plt.imshow(img_md1)
plt.title("Imagen modificada 1")
plt.show()

Imagen_md1 = Image.fromarray(img_md1)

# B) En una imagen nueva(imagen modificada)
# presentar en un subplot arriba la negativa
# Su c, m, Y

#CMY
img1_5 = np.zeros((1080,1920,3), dtype=np.uint8) #Imagen negativa
img1_6 = np.zeros((1080,1920,3), dtype=np.uint8)
img1_7 = np.zeros((1080,1920,3), dtype=np.uint8)
img1_8 = np.zeros((1080,1920,3), dtype=np.uint8)

#Conversion a espacio CMY

img1_5[:,:,0]=255-img_md1[:,:,0]
img1_5[:,:,1]=255-img_md1[:,:,1]
img1_5[:,:,2]=255-img_md1[:,:,2]

#Cyan
red = 255-img_md1[:,:,0]
green = 255
blue = 255

img1_6[:,:,0]=red
img1_6[:,:,1]=green
img1_6[:,:,2]=blue

#Magenta
red = 255
green = 255-img_md1[:,:,1]
blue = 255

img1_7[:,:,0]=red
img1_7[:,:,1]=green
img1_7[:,:,2]=blue

#Yellow
red = 255
green = 255
blue = 255-img_md1[:,:,2]

img1_8[:,:,0]=red
img1_8[:,:,1]=green
img1_8[:,:,2]=blue

f, axes = plt.subplots(2,2, constrained_layout = True)

#Imagen modificada 1 - negativo
axes[0, 0].title.set_text('Imagen modificada 1 - negativa')
axes[0, 0].imshow(img1_5)

#Imagen modificada 1 - cyan
axes[0, 1].title.set_text('Imagen modificada 1 - color cyan')
axes[0, 1].imshow(img1_6)

#Imagen modificada 1 - magenta
axes[1, 0].title.set_text('Imagen modificada 1 - color magenta')
axes[1, 0].imshow(img1_7)

#Imagen modificada 1 - yellow
axes[1, 1].title.set_text('Imagen modificada 1 - color amarillo')
axes[1, 1].imshow(img1_8)
plt.show()

# C) Mostrar el histograma de la escala de grises

imgmd_gris1 = Imagen_md1.convert('L')
histgray = imgmd_gris1.histogram()
plt.plot(histgray, color='gray')

plt.xlabel('Intensiddad')
plt.ylabel('Cantidad de pixeles')
plt.show()

# D) Subplot de la imagen invertida en el eje x - horizontal
# Imagen invertida en y - vertical
# Imagen rotada 

f, axes = plt.subplots(2,2, constrained_layout = True)

#Imagen modificada 1 
axes[0, 0].title.set_text('Imagen modificada 1')
axes[0, 0].imshow(img_md1)

#Imagen modificda 1 - invertida en el eje x (Horizontal)
#horizontal = Imagen_md1.transpose(Image.FLIP_LEFT_RIGHT)
horizontal = Image.fromarray(np.fliplr(img_md1))
axes[0, 1].title.set_text('Imagen modificada 1 - invertida en el eje x')
axes[0, 1].imshow(horizontal)

#Imagen modificada 1 - invertida en el eje y (Vertical)
vertical = Imagen_md1.transpose(Image.FLIP_TOP_BOTTOM)
axes[1, 0].title.set_text('Imagen modificada 1 - invertida en el eje y')
axes[1, 0].imshow(vertical)

#Imagen modificada 1 - rotada
axes[1, 1].title.set_text('Imagen modificada 1 - rotada')
axes[1, 1].imshow(Imagen_md1.rotate(45))

plt.show()