# Elaborado por César Alejandro Villegas Espíndola
# Fecha_ Jueves 1 de diciembre del 2022

from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from PIL import Image, ImageFilter
import numpy as np
from numpy import asarray

img = Image.open('/Users/cvillegas/workspace/Py/DIP/Ejercicio 9/car.jpg')

plt.imshow(img)
plt.show()

img_gris = img.convert('L')

# Filtro de la mediana
new_img = img_gris.filter(ImageFilter.MedianFilter(3))
plt.imshow(new_img, cmap='gray')
plt.show()

# Filtro Gaussiano
# Le quita el ruido fino y constante
FILTRO_GAUSSIANO = new_img.filter(ImageFilter.GaussianBlur)
FILTRO_GAUSSIANO.show()

# Filtro Gausseano con cambio del tamaño de la mascara
FILTRO_GAUSSIANO = new_img.filter(ImageFilter.GaussianBlur)
FILTRO_GAUSSIANO.show()

# Filtro laplaceano
# Esta basado en la derivada, se ve el cambio entre pixeles, i es cambio es borde, por lo cual se utilizara para detección de bordes. Este cambia los valores de las mascaras. 
# Se definira una mascara. A continuación se elaborará una matriz
mascara = [0, 0, -1, 0, 0, 0, -1, -2, -1, 0, -1, -2, 16, -2, -1, 0, -1, -2, -1, 0, 0, 0, -1, 0, 0]
filtro_Laplaceano = new_img.filter(ImageFilter.Kernel((5,5), mascara,1))
filtro_Laplaceano.show()

# Mascara Especial Prewit - Horizontal
mascaraH = [-1,-1,-1,0,0,0,1,1,1]
Filtro_PrewithH = img_gris.filter(ImageFilter.Kernel((3,3),mascaraH,5))
Filtro_PrewithH.show()

# Mascara Especial Prewit - Vertical
mascaraV = [-1,0,1,-1,0,1,-1,0,1]
Filtro_PrewithV = img_gris.filter(ImageFilter.Kernel((3,3),mascaraV,3))
Filtro_PrewithV.show()

#Mascara Especial Sobel - Horizontal
mascaraSH = [-1,-2,-1,0,0,0,1,2,1]
Filtro_SobelH = img_gris.filter(ImageFilter.Kernel((3,3),mascaraSH,3))
Filtro_SobelH.show()

#Mascara Especial Sobel - Vertical
mascaraSV = [-1,0,1,-2,0,2,-1,0,1]
Filtro_SobelV = img_gris.filter(ImageFilter.Kernel((3,3),mascaraSV,3))
Filtro_SobelV.show()

Image.blend(Filtro_SobelH, Filtro_SobelH, 0.5)