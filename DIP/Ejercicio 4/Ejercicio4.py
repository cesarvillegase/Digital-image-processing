# Histograma mediante librería PIL
#Elaborado por César Alejandro Villegas Espíndola

# Se importo desde PIL imagen
from PIL import Image
from matplotlib import pyplot as plt #De igual manera se puede importar como from matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
from sklearn.metrics import homogeneity_completeness_v_measure

img = Image.open('/Users/cvillegas/workspace/Py/DIP/Ejercicio 4/Cat4.jpg')
img_gris = img.convert('L')
hist=img_gris.histogram()
plt.plot(hist, color='gray')

plt.xlabel('Intensiddad')
plt.ylabel('Cantidad de pixeles')
plt.show()

#img = Image.open('/Users/cvillegas/workspace/Py/DIP/Ejercicio 4/Cat4.jpg')
#histograma=np.zeros(256)
#print(histograma)

#Dimensiones de la imagen 2048 × 2048
img = mpimg.imread('/Users/cvillegas/workspace/Py/DIP/Ejercicio 4/Cat4.jpg')
img_gris = 0.2989*img[:,:,0] + 0.5870*img[:,:,1] + 0.1140*img[:,:,2]

histograma=np.zeros(256)
print(img_gris[2, 2, 0]) # Prueba de acceso al arreglo
for i in range(2049):
    for j in range(2049):
        histograma[img_gris[i,j]] = histograma[img_gris[i,j]] + 1
print(histograma)