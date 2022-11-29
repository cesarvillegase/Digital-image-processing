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

############################################################################################################################################

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

############################################################################################################################################

# MEDIANA
# Se itera por cada parte de la matriz
# Se hace nuevamente una copia de img
img_filtrada1 = img.copy()
data = asarray(img_filtrada1)

for i in range(largo-1):
    for j in range(ancho-1):
      temp = [img_gris[i-1, j-1], img_gris[i, j-1], img_gris[i+1, j-1], img_gris[i-1, j], img_gris[i, j], img_gris[i+1, j], img_gris[i-1, j+1], img_gris[i-1, j+1], img_gris[i+1, j+1]]
      temp = sorted(temp)
      img_filtrada1[i,j] = temp[4]
      
mediana = Image.fromarray(img_filtrada1)
img_filtrada1
            
plt.imshow(img_filtrada1)
plt.title("Mediana")
plt.show()

############################################################################################################################################

# MINIMO
# Se itera por cada parte de la matriz
# Nuevamente se hace una copia de img llamada img_filtrada2
img_filtrada2 = img.copy()

for i in range(1,largo-1):
    for j in range(1,ancho-1):
        temp = [img_gris[i-1, j-1], img_gris[i, j-1], img_gris[i+1, j-1], 
                img_gris[i-1, j], img_gris[i, j], img_gris[i+1, j],
                img_gris[i-1, j+1],img_gris[i-1, j+1], img_gris[i+1, j+1]]
        temp=min(temp)
        img_filtrada2[i,j] = temp

plt.imshow(img_filtrada2)
plt.title("Minimo")
plt.show()

############################################################################################################################################

# MAXIMO
# Nuevamente se itera por cada parte de la matriz
# Y se hace una copia de img llamada img_filtrada3
img_filtrada3 = img.copy()

for i in range(1,largo-1):
    for j in range(1,ancho-1):
        temp = [img_gris[i-1, j-1], img_gris[i, j-1], img_gris[i+1, j-1],
        img_gris[i-1, j], img_gris[i, j], img_gris[i+1, j], 
        img_gris[i-1, j+1], img_gris[i-1, j+1], img_gris[i+1, j+1]]
        temp=max(temp)
        img_filtrada3[i,j] = temp

plt.imshow(img_filtrada3)
plt.title("Maximo")
plt.show()