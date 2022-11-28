#Ejercicio 8 - Filtros digitales
#Elaborado por César Alejandro Villegas Espíndola
#Fecha: Lunes 28 de noviembre del 2022

#Importación de librerias
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np

img = mpimg.imread('/Users/cvillegas/workspace/Py/DIP/Ejercicio 8/saltandpeppernoise.jpg')

print(img)

plt.imshow(img)
plt.title("Imagen con ruido de sal y pimienta")
plt.show()

print(img.shape)

ancho = img.shape[0]
print(ancho)

largo = img.shape[1]
print(largo)

img_filtrada = img.copy()

Imagen_ft = Image.fromarray(img_filtrada)

#MEDIA

mascara = np.ones([3,3], dtype=int)
mascara = mascara/9
for i in range(ancho-1):
    for j in range(largo-1):
        img_filtrada[i,j] = img[i-1, j-1] * mascara[0,0] + img[i, j-1] * mascara[0,1] + img[i+1, j-1] * mascara[0,2] 
        + img[i-1, j] * mascara[1,0] + img[i, j] * mascara[1,1] + img[i+1, j] * mascara[1,2] 
        + img[i-1, j+1] * mascara[2,0] + img[i-1, j+1] * mascara[2,1] + img[i+1, j+1] * mascara[2,2]
        
plt.imshow(img_filtrada)
plt.title("Media")
plt.show()

#MEDIANA

img_filtrada1 = img.copy()

Imagen_ft1 = Image.fromarray(img_filtrada1)

for i in range(ancho-1):
    for j in range(largo-1):
        temp = [img[i-1, j-1], img[i, j-1], img[i+1, j-1],
        img[i-1, j], img[i, j], img[i+1, j], 
        img[i-1, j+1], img[i-1, j+1], img[i+1, j+1]]
        temp=sorted(temp)
        Imagen_ft1[i,j] = temp[4]
        
        
plt.imshow(Imagen_ft1)
plt.title("Mediana")
plt.show()