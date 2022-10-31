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

# Histograma en rojo
histograma1=np.zeros(256)
#print() # Prueba de acceso al arreglo
for i in range(2048):
    for j in range(2048):
        histograma1[img[i,j,0]] = histograma1[img[i,j,0]] + 1
print(histograma1)
plt.plot(histograma1, color='red')
plt.xlabel('Intensidad')
plt.ylabel('Cantidad de pixeles')
#plt.show()

#Histograma en verde
histograma2=np.zeros(256)
#print() # Prueba de acceso al arreglo
for i in range(2048):
    for j in range(2048):
        histograma2[img[i,j,1]] = histograma2[img[i,j,1]] + 1
print(histograma2)
plt.plot(histograma2, color='green')
plt.xlabel('Intensidad')
plt.ylabel('Cantidad de pixeles')
#plt.show()

# Histograma en azul
histograma3=np.zeros(256)
#print() # Prueba de acceso al arreglo
for i in range(2048):
    for j in range(2048):
        histograma3[img[i,j,2]] = histograma3[img[i,j,2]] + 1
print(histograma3)
plt.plot(histograma3, color='blue')
plt.xlabel('Intensidad')
plt.ylabel('Cantidad de pixeles')

plt.show()