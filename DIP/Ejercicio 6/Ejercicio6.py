#Ejercicio 2 - Manipulación de imágenes e información
#Elaborado por César Alejandro Villegas Espíndola
#Fecha: Jueves 3 de noviembre del 2022

#Importación de librerias 
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

##########################Ejercicio1##########################

#Imagen 1 - Sumar imagen + negativo 

#Se carga la imagen 
img = mpimg.imread('/Users/cvillegas/workspace/Py/DIP/Ejercicio 6/Cat.jpg')

img_ng = np.zeros((720,1080,3), dtype=np.uint8) #Imagen completa en negativo

img_ng[:,:,0]=255-img[:,:,0]
img_ng[:,:,1]=255-img[:,:,1]
img_ng[:,:,2]=255-img[:,:,2]

img1 = img +  img_ng

plt.imshow(img1)
plt.title("Imagen editada - ejercicio 1")
plt.show()

#Se separan los espacios de color

img = mpimg.imread('/Users/cvillegas/workspace/Py/DIP/Ejercicio 6/Cat.jpg')

img1_2 = np.zeros((720,1080,3), dtype=np.uint8)
img1_3 = np.zeros((720,1080,3), dtype=np.uint8)
img1_4 = np.zeros((720,1080,3), dtype=np.uint8)

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
red = 0*img[:,:,0]
green = 0*img[:,:,1]
blue = img[:,:,2]

img1_4[:,:,0]=red
img1_4[:,:,1]=green
img1_4[:,:,2]=blue

#CMY
img1_5 = np.zeros((720,1080,3), dtype=np.uint8) 
img1_6 = np.zeros((720,1080,3), dtype=np.uint8)
img1_7 = np.zeros((720,1080,3), dtype=np.uint8)
img1_8 = np.zeros((720,1080,3), dtype=np.uint8)

#Conversion a espacio CMY

img1_5[:,:,0]=255-img[:,:,0]
img1_5[:,:,1]=255-img[:,:,1]
img1_5[:,:,2]=255-img[:,:,2]

#Cyan
red = 255-img[:,:,0]
green = 255
blue = 255

img1_6[:,:,0]=red
img1_6[:,:,1]=green
img1_6[:,:,2]=blue

#Magenta
red = 255
green = 255-img[:,:,1]
blue = 255

img1_7[:,:,0]=red
img1_7[:,:,1]=green
img1_7[:,:,2]=blue

#Yellow
red = 255
green = 255
blue = 255-img[:,:,2]

img1_8[:,:,0]=red
img1_8[:,:,1]=green
img1_8[:,:,2]=blue

#Imagen 2 - Red + Cyan
imag2 = img1_2 + img1_6
plt.imshow(imag2)
plt.title("Ejercicio 1 - Imagen editada 2")
plt.show()

#Imagen 3 - Green + Magenta
imag3 = img1_3 + img1_7
plt.imshow(imag3)
plt.title("Ejercicio 1 - Imagen editada 3")
plt.show()

#Imagen 4 - blue + Yellow
imag4 = img1_4 + img1_8
plt.imshow(imag4)
plt.title("Ejercicio 1 - Imagen editada 4")
plt.show()

##########################Ejercicio2##########################

#Se carga la imagen 
img = mpimg.imread('/Users/cvillegas/workspace/Py/DIP/Ejercicio 6/Cat.jpg')

#Separar cada canal

imagen2 = np.zeros((720,1080,3), dtype=np.uint8) #Imagen completa

imagen2[:,:,0]=255*img[:,:,0]
imagen2[:,:,1]=255*img[:,:,1]
imagen2[:,:,2]=255*img[:,:,2]

print(imagen2[719,1,2])
print(255*img[719,1,2])

img_st = img.copy()

for i in range(720):
  for j in range(1080):
    if (img[i,j,0]*2 > 255):
      img_st[i,j,0] = 255
    else :
        img_st[i,j,0] = img[i,j,0]*2
    if (img[i,j,1]*2 > 255):
      img_st[i,j,1] = 255
    else :
      img_st[i,j,1] =img[i,j,1]*2
    if (img[i,j,2]*2 > 255):
      img_st[i,j,2] = 255
    else :
      img_st[i,j,2] =img[i,j,2]*2

Imagen_st = Image.fromarray(img_st)

#Imagen original
plt.subplot(311)
plt.imshow(img)
plt.title("Imagen original")

#Imagen saturada - imagen2
plt.subplot(312)
plt.imshow(img_st)
plt.title("Imagen editada ejercicio 2")

plt.show()

#Histograma Gray - Imagen

img = Image.open('/Users/cvillegas/workspace/Py/DIP/Ejercicio 6/Cat.jpg')
img_gris = img.convert('L')
hist=img_gris.histogram()
plt.plot(hist, color='gray')

plt.xlabel('Intensiddad')
plt.ylabel('Cantidad de pixeles')
plt.show()

#Histograma Gray - Imagen2

img_gris2 = Imagen_st.convert('L')
hist2=img_gris2.histogram()
plt.plot(hist2, color='gray')

plt.xlabel('Intensiddad')
plt.ylabel('Cantidad de pixeles')
plt.show()

#Histograma 3Colores - Imagen2

img = mpimg.imread('/Users/cvillegas/workspace/Py/DIP/Ejercicio 6/Cat.jpg')

#Color rojo
histograma3 = np.zeros(256)
for i in range(720):
  for j in range(1080):
    histograma3[img[i,j,0]] = histograma3[img[i,j,0]] + 1
print(histograma3)
plt.plot(histograma3, color='red')
plt.xlabel('Intensidad')
plt.ylabel('Cantidad de pixeles')

#Color verde
histograma4 = np.zeros(256)
for i in range(720):
    for j in range(1080):
        histograma4[img[i,j,1]] = histograma4[img[i,j,1]] + 1
print(histograma4)
plt.plot(histograma4, color='green')
plt.xlabel('Intensidad')
plt.ylabel('Cantidad de pixeles')

#Color azul
histograma5 = np.zeros(256)
for i in range(720):
  for j in range(1080):
        histograma5[img[i,j,2]] = histograma5[img[i,j,2]] + 1
print(histograma5)
plt.plot(histograma5, color='blue')
plt.xlabel('Intensidad')
plt.ylabel('Cantidad de pixeles')

plt.show()

#Histograma 3Colores - Imagen

#Color rojo
histograma6 = np.zeros(256)
for i in range(720):
  for j in range(1080):
    histograma6[img_st[i,j,0]] = histograma6[img_st[i,j,0]] + 1
#print(histograma6)
plt.plot(histograma3, color='red')
plt.xlabel('Intensidad')
plt.ylabel('Cantidad de pixeles')

#Color verde
histograma7 = np.zeros(256)
for i in range(720):
    for j in range(1080):
        histograma7[img_st[i,j,1]] = histograma7[img_st[i,j,1]] + 1
#print(histograma7)
plt.plot(histograma7, color='green')
plt.xlabel('Intensidad')
plt.ylabel('Cantidad de pixeles')

#Color azul
histograma8 = np.zeros(256)
for i in range(720):
  for j in range(1080):
        histograma8[img_st[i,j,2]] = histograma8[img_st[i,j,2]] + 1
#print(histograma8)
plt.plot(histograma8, color='blue')
plt.xlabel('Intensidad')
plt.ylabel('Cantidad de pixeles')

plt.show()

##########################Ejercicio3##########################

f, axes = plt.subplots(2,2, constrained_layout = True)

#Imagen original
axes[0, 0].title.set_text('Imagen original')
axes[0, 0].imshow(img)

#Imagen2 rotada 30º
axes[0, 1].title.set_text('Imagen rotada a 30 grados')
axes[0, 1].imshow(Imagen_st.rotate(30))

#Imagen2 - Mirror x y rotada 60º y a 300 x 300
img_rs = Imagen_st.resize((300,300))
img_st_mr = Image.fromarray(np.flip(img_rs, (0, 1)))
axes[1, 0].title.set_text('Imagen rotada a 60 grados y con mirror')
axes[1, 0].imshow(img_st_mr.rotate(60))
plt.show()