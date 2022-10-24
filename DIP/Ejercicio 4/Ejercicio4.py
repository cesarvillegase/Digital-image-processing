# Histograma mediante librería PIL
#Elaborado por César Alejandro Villegas Espíndola

# Se importo desde PIL imagen
from PIL import Image
from matplotlib import pyplot as plt #De igual manera se puede importar como from matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

img = Image.open('/Users/cvillegas/workspace/Py/DIP/Ejercicio 4/Cat4.jpg')
img_gris = img.convert('L')
hist=img_gris.histogram()
plt.plot(hist, color='gray')

plt.xlabel('Intensiddad')
plt.ylabel('Cantidad de pixeles')
plt.show()

img = Image.open('/Users/cvillegas/workspace/Py/DIP/Ejercicio 4/Cat4.jpg')
histograma=np.zeros(256)
print(histograma)

img = mpimg.imread('/Users/cvillegas/workspace/Py/DIP/Ejercicio 4/Cat4.jpg')

