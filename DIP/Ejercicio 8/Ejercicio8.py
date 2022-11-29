# Ejercicio 8 - Filtros digitales
# Elaborado por César Alejandro Villegas Espíndola
# Fecha: Lunes 28 de noviembre del 2022

# Importación de librerias
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np
from numpy import asarray

img = mpimg.imread('/Users/cvillegas/workspace/Py/DIP/Ejercicio 8/saltandpeppernoise.jpg')

print(img)

# Se separan los espacios de color

R=img[:,:,0]
G=img[:,:,1]
B=img[:,:,2]

img_gris = 0.2989*R+0.5810*G+0.1140*B

# Se muestra la imagen en escala de grises

plt.imshow(img_gris, cmap='gray')
plt.title("Imagen con ruido de sal y pimienta")
plt.show()

# Se imprime la forma de la imagen

print(img.shape)

ancho = img.shape[0]
print(ancho)

largo = img.shape[1]
print(largo)

img_filtrada = img.copy()

# Media
# Se itera por cada parte de la matriz
mascara = np.ones([3,3], dtype=int)
mascara = mascara/9
for i in range(ancho-1):
    for j in range(largo-1):
        img_filtrada[i,j] = img_gris[i-1, j-1] * mascara[0,0] + img_gris[i, j-1] * mascara[0,1] + img_gris[i+1, j-1] * mascara[0,2] 
        + img_gris[i-1, j] * mascara[1,0] + img_gris[i, j] * mascara[1,1] + img_gris[i+1, j] * mascara[1,2] 
        + img_gris[i-1, j+1] * mascara[2,0] + img_gris[i-1, j+1] * mascara[2,1] + img_gris[i+1, j+1] * mascara[2,2]
        
plt.imshow(img_filtrada)
plt.title("Media")
plt.show()

# MEDIANA
# Se itera por cada parte de la matriz
# Se hace nuevamente una copia de img
img_filtrada1 = img.copy()
data = asarray(img_filtrada1)

for i in range(ancho-1):
    for j in range(largo-1):
        temp = [img[i-1, j-1], img[i, j-1], img[i+1, j-1],img[i-1, j], img[i, j], img[i+1, j], img[i-1, j+1], img[i-1, j+1], img[i+1, j+1]]
        temp=sorted(temp)
        Imagen_ft1[i,j] = temp[4]
            
plt.imshow(Imagen_ft1)
plt.title("Mediana")
plt.show()

# MINIMO

for i in range(1,largo-1):
    for j in range(1,ancho-1):
        temp = [img[i-1, j-1], img[i, j-1], img[i+1, j-1],
        img[i-1, j], img[i, j], img[i+1, j], 
        img[i-1, j+1], img[i-1, j+1], img[i+1, j+1]]
        temp=min(temp)
        Imagen_ft1[i,j] = temp

plt.imshow(Imagen_ft1)
plt.title("Minimo")
plt.show()

# MAXIMO

for i in range(1,largo-1):
    for j in range(1,ancho-1):
        temp = [img[i-1, j-1], img[i, j-1], img[i+1, j-1],
        img[i-1, j], img[i, j], img[i+1, j], 
        img[i-1, j+1], img[i-1, j+1], img[i+1, j+1]]
        temp=max(temp)
        Imagen_ft1[i,j] = temp

plt.imshow(Imagen_ft1)
plt.title("Maximo")
plt.show()